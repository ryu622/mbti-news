#タイトル 
mbti-news

#概要・背景 
apiを作ってフロントエンドとバックエンドに分けた開発をしたいと思い、そのためにまず練習としてflaskにて外部apiと連携したNEWS検索アプリを作成した。今mbtiが流行っているのでそれと組み合わせたアプリを作れないかと以前から考えており、今回mbtiとニュースを組み合わせ、mbtiを入れるとそのmbtiにマッチしたニュースを表示するようにした。デザインはcssでシンプルで見やすいようにした。バリデーション機能も追加した。このアプリ作成の過程でrequestでHTMLからキーワードを受け取り、requestsで外部apiを叩いて情報取得するという一連の流れを学べた。また、apiから送られて来るデータの形式（JSON）とその利用方法を学べた。さらに、以前まではFlask-WTFを用いてフォームとバリデーションを実装していたが、今回はシンプルにHTMLのinputタグを使用した（Flask-WTFを使っていない）。そのため、Flask-WTFを使わないrequestを用いた基本的なバリエーション機能の実装を学んだ。

#インストール方法 git clone https://github.com/ryu622/mbti-newsgit cd news-api-search pip install -r requirements.txt

#使用方法 
入力欄にmbtiを入れると、それに合うニュースが出力されます。ページ下部の「次へ」を押すと次のページへ、「前へ」を押すと前のページへ遷移します。

#機能一覧 
・NEWSapiを叩いてキーワードを含むニュースを取得
・（SQLインジェクション対策として）バリデーション機能

#開発環境・技術スタック 
Python,Flask,HTML,CSS

#ライセンス 
MIT License

#作成者 
https://github.com/ryu622
