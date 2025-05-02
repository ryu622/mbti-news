import requests
from flask import Flask,render_template,request
import os
from dotenv import load_dotenv

# 環境変数に設定したAPIKeyを使うために.envファイルを読み込む
load_dotenv()


#インスタンス生成
app=Flask(__name__)

app.config['MY_APIKEY'] =os.getenv('MY_APIKEY')

#ルーティング
@app.route('/')
def index():
    #HTMLから変数を取得
    mbti=request.args.get("mbti")
    #mbtiごとにジャンルを決定
    if mbti=='INTJ':
        keyword='futurism'
    elif mbti=='INTP':
        keyword='artificial intelligence'
    elif mbti=='ENTJ':
        keyword='leadership'
    elif mbti=='ENTP':
        keyword='startups'
    elif mbti=='INFJ':
        keyword='psychology'
    elif mbti=='INFP':
        keyword='creative writing'
    elif mbti=='ENFJ':
        keyword='education reform'
    elif mbti=='ENFP':
        keyword='social innovation'
    elif mbti=='ISTJ':
        keyword='economic policy'
    elif mbti=='ISFJ':
        keyword='public health'
    elif mbti=='ESTJ':
        keyword='corporate management'
    elif mbti=='ESFJ':
        keyword='community service'
    elif mbti=='ISTP':
        keyword='engineering'
    elif mbti=='ISFP':
        keyword='modern art'
    elif mbti=='ESTP':
        keyword='extreme sports'
    elif mbti=='ESFP':
        keyword='celebrity news'
    else:
        keyword='general'
    page = request.args.get("page", default=1, type=int)
    
    #先にリストを定義しておく
    articles=[]
    #バリデーション機能
    #バリデーション用のエラーを入れるリスト
    errors=[]
    #キーワードが空でなければ処理
    if mbti:
        if not (mbti.isalpha() and mbti.isupper()):
            errors.append("英大文字（A〜Z）のみで入力してください（例：INFP）")
        else:
            #クエリパラメータ
            params = {
                    'q':keyword,
                    'language': 'en',
                    'pageSize': 5,
                    'page': page,
                    'apiKey': app.config['MY_APIKEY']
                }
            #apiにリクエストを送る
            res = requests.get('https://newsapi.org/v2/everything', params=params)
            #json形式で受け取る
            res_json = res.json()
            #ほしい項目だけリストに格納
            for article in res_json['articles']:
                articles.append({
            'title': article['title'],
            'description':article['description'],
            'image': article['urlToImage'],
            'url':article['url']
            })
            print(articles)
    else:
            print('準備OK')
    
    
    return render_template('index.html',articles=articles,mbti=mbti,page=page,errors=errors,keyword=keyword)


#実行
if __name__=='__main__':
    app.run()


