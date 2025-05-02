#タイトル 
news-api-search

#概要・背景 
apiを作ってフロントエンドとバックエンドに分けた開発をしたいと思い、そのためにまず練習としてflaskにて外部apiと連携したNEWS検索アプリを作成した。デザインはcssでシンプルで見やすいようにした。このアプリ作成の過程でrequestでHTMLからキーワードを受け取り、requestsで外部apiを叩いて情報取得するという一連の流れを学べた。また、apiから送られて来るデータの形式（JSON）とその利用方法を学べた。

#インストール方法 git clone https://github.com/ryu622/news-api-search.git cd news-api-search pip install -r requirements.txt

#使用方法 
検索バーに検索語句を入れると、それを含むニュースが出力されます。ページ下部の「次へ」を押すと次のページへ、「前へ」を押すと前のページへ遷移します。

#機能一覧 
・NEWSapiを叩いてキーワードを含むニュースを取得

#開発環境・技術スタック 
Python,Flask,HTML,CSS

#ライセンス 
MIT License

#作成者 
https://github.com/ryu622
