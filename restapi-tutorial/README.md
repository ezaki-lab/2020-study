# 研究室ゼミ REST API 【Python FlaskでREST APIを実装】

# 実行日
2020/4/17

今回の説明はqiitaにて限定公開しているため、github上で見にくい場合は下記のqiitaの方へ飛んでください

[REST API qiita](https://qiita.com/YutoTakamatsu/private/44869f28a841604e42a5)

# RESTAPIの概要

## REST APIとは

>RESTful API(REST API)とは、Webシステムを外部から利用するためのプログラムの呼び出し規約(API)の種類の一つで、RESTと呼ばれる設計原則に従って策定されたもの。RESTそのものは適用範囲の広い抽象的なモデルだが、一般的にはRESTの考え方をWeb APIに適用したものをRESTful APIと呼んでいる。

>RESTful APIでは、URL/URIですべてのリソースを一意に識別し、セッション管理や状態管理などを行わない(ステートレス)。同じURLに対する呼び出しには常に同じ結果が返されることが期待される。

>また、リソースの操作はHTTPメソッドによって指定(取得ならGETメソッド、書き込みならPOSTメソッド)され、結果はXMLやHTML、JSONなどで返される。また、処理結果はHTTPステータスコードで通知するという原則が含まれることもある。

引用：[IT用語辞典 e-Words](http://e-words.jp/w/RESTful_API.html)

システムの設計原則(設計の考え方)の一つです。元々はAPIに限らずウェブ全体に適用するための考え方です。
このRESTの考え方に従って設計されたAPIを REST API と言います。

## 一般的なRESTの特徴

#### REST APIの特徴
 * URI(HTTPのパス)が名詞形であること（動詞を含まないこと）
 * リソース（操作対象のもの）の操作（作成/閲覧/変更/削除）をHTTPのメソッドにより指定できること
 * レスポンス形式がjsonもしくはXMLであること
 
#### URLとURIの違い（特に違いはない）
<img src = "https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/517357/623f7511-785b-b0cc-5a18-a7bff14c1999.jpeg" width = "500px">

細かいことを言うと「http:」というパーツはURLとして定められているわけではなく、URIとしての識別子（スキーム）なので、技術仕様などではURIと呼ぶことが多いです。

### REST APIの例
|やりたいこと|URL|HTTPのメソッド|
|:-----------:|:------------|:------------:|
|ユーザ一覧確認|https://APIサーバのホスト名/users|GET|
|ユーザ新規登録|https://APIサーバのホスト名/users|POST|
|ユーザ変更|https://APIサーバのホスト名/users/ユーザID|PUT|
|ユーザ削除|https://APIサーバのホスト名/users/ユーザID|DELETE|

詳細を説明していく前に、比較するためにRESTではないAPIの例を出します。

### RESTではないAPIの例
|やりたいこと|URL|HTTPのメソッド|
|:-----------:|:------------|:------------:|
|ユーザ一覧確認|https://APIサーバのホスト名/get_users|GET|
|ユーザ新規登録|https://APIサーバのホスト名/create_user|GET|
|ユーザ変更|https://APIサーバのホスト名/modify_users|GET|
|ユーザ削除|https://APIサーバのホスト名/delete_users|GET|

### RESTなAPIとそうでないAPI
ユーザ情報を確認、登録、変更、削除を行う場合のAPIを作成しようと考える。

![RESTではない.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/517357/c605c848-0b81-9c78-d4b1-12228a6a682c.png)

処理にURLが対応づくようなシステムを思い浮かべると思います。

たとえば、更新を行う場合、更新用URLを発行し、セッションなどに保持された情報を用いてリクエスト処理を行うといったものです。

しかし、これはRESTなAPIではありません。
RESTなAPIはリソースに対応づいてURLが決まる。処理にはURLは対応づかないのです。

同じシステムを考えた時に、RESTなAPIの場合はユーザ情報にURLが対応づく。
RESTな考えで同じシステムを構築した場合はこのようになります。

![RESTAPI.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/517357/96221ea7-77b9-6a0a-1f9b-9259ecb47c14.png)

上記の処理では、ユーザ情報の作成・取得・更新・削除に対して一つの「/users」をURLに対応づけしている。

確認、登録、変更、削除については、HTTPの一般的なリクエストメソッドを使用し、「GET」なら確認、「POST」なら登録、「PUT」なら変更、DELETE」なら削除のように処理を決定する。

HTTPの一般的なリクエストメソッドを使用することもRESTなAPIである一つの要因である。

#### HTTPの一般的なリクエストメソッドとは

HTTPリクエストメソッドとは、Webブラウザからwebサーバに対しての命令（リクエスト）です。

Webブラウザは、Webサーバから情報をもらって画面に出力しています。

<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/517357/bd1d0b2d-ca6d-779e-13b4-18c22cd356c7.jpeg" width="400px">
図解するとこのような感じです。
これはGETの例です。
1. ユーザがWebブラウザで検索
2. ブラウザがwebサーバに命令（リクエスト）
3. WebサーバがWebブラウザにアクション
4. ユーザの元に画像が表示される

|リクエストメソッド|説明|していること|重要度|
|:-----------:|:------------|:------------|:------------:|
|GET|リソースの要求|Webサーバに閲覧したい情報を取得|◎|
|POST|リソースの送信|Webサーバにファイルを送信|◎|
|PUT|リソースの更新（置き換え）|Webサーバにファイルを送信(基本的にはPOSTを使用)|◎|
|DELETE|リソースの削除|Webサーバにあるファイルやデータの削除|◎|
|HEAD|リソースの（ヘッダだけ）の要求|Webサーバのヘッダデータのみを取得|○|
|OPTIONS|サーバの調査|Webサーバでどのメソッドが利用できるかがわかる|○|
|CONNECT|トンネルを開く|データのパケットをサーバまで転送|△|
|TRACE|ネットワーク経路の調査|Webサーバと接続ができるかの確認|○|

#### リクエストメソッド：GET
<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/517357/71089675-1e0c-518e-53b4-62d0ef9ba287.jpeg" width="400px">

初めてみるWebサイトを表示する時に<font color="Red">GET</font>が行われています。


#### リクエストメソッド：POST
<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/517357/0455aeaa-f450-4953-2015-1c579dce4abb.jpeg" width="400px">

データをWebサーバに提供します。
例えば、何かのサイトの会員情報を登録する時、<font color="Red">POST</font>が行われます。
会員情報を入力して、会員情報を確定するを押した瞬間にPOSTが行われ、Webサーバに会員情報が渡されます。

#### リクエストメソッド：PUT
<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/517357/5e7208df-6876-5c45-6718-db810ec93a2e.jpeg" width="400px">

<font color="Red">PUT</font>は、リソースの更新をします。
例えば、記事を投稿したり、編集して更新したりすると、PUTが行われます。

#### リクエストメソッド：DELETE
<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/517357/171fe37f-50f5-f5b1-e636-baea43f166ed.jpeg" width="400px">

<font color="Red">DELETE</font>は、データを削除する時に使用します。

他のリクエストメソッドに関しては、あまり使うことがないので、気になる人は自分で調べてみてください。

## URI(HTTPのパス）が名詞形であること（動詞を含まないこと）
これは、先程の例で言えばREST APIの場合、URIは /users、 非RESTの場合は /get_users のようになっていました。
このように URIが名詞形だけであること がREST APIの特徴です。
一つのURIしかないのに、どうやって作ったり消したりするの？

## リソースの操作をHTTPのメソッドにより指定できること
HTTPのメソッドを変えることで作る、消すなどの操作を変えるということができます。
つまり、同じURLにアクセスした場合でも、HTTPのメソッドが違うと異なる動作をするということです。
(ちなみにHTTPのメソッドというのは、HTTPのリクエストに含めることができる情報の一つです。)

GETメソッドでアクセスする -> ユーザ一覧を返す
POSTメソッドでアクセスする -> ユーザを新規作成する

のように動作します。具体例としてcurlコマンドで言うと、

```
# ユーザ一覧取得
curl -X GET https://サーバのAPI/users

# ユーザ新規作成
curl -X POST https://サーバのAPI/users
```
のようになります。
#### curlとは
curlとはCLI【コマンドラインインターフェース / Command Line Interface】または、CUI【キャラクタユーザインターフェース / Character User interface】でHTTPリクエストなどを実行するためのコマンドです。


各メソッドの動作の関係ですが、一般的には先程説明したように

|メソッド|動作|(参考）SQLでの動作名|
|:-----------|:------------|:------------|
|GET|リソース情報の取得|select|
|POST|リソース新規作成|insert|
|PUT/PATCH|リソース更新|updata|
|DELETE|リソース削除|delete|
のようにメソッド割り当てられています。

## レスポンス形式がjsonもしくはXMLであること
書いてある通りなのですが、サーバからのレスポンスがjsonかXML形式で返ってくることです。
最近のWebAPIはほとんどjsonになっていると思います。(XMLはあまりみない）

## 有名なREST API
例えば、TwitterやFaceBookのAPIとして提供されています。

Twitter APIで検索すると以下のようにわかりやすい解説をしてくれるサイトがあります。

[Twitter公式](https://developer.twitter.com/en)
[Twitter REST APIの使い方](https://syncer.jp/Web/API/Twitter/REST_API/)

FaceBookについてはGraph APIというものが提供されています。
[FaceBook公式](https://developers.facebook.com/docs/graph-api)

さらに、GithubもAPIを出しているので、興味のある人は調べてみてください。
[Github API](https://developer.github.com/v3/)

# 【Python FlaskでREST APIを実装する】

## Flask とは
[Flask](https://a2c.bitbucket.io/flask/)は、Webフレームワークで軽量で機能がそこまで備わっていないということが最大の特徴です。
Webフレームワークというと、Rubyの[Rails](https://rubyonrails.org)やPythonでは[Django](https://www.djangoproject.com)などが有名ですが、機能が多いためFlaskに比べるとかなり重いというデメリットがあります。

FlaskはPythonのWebアプリケーションフレームワークで、小規模向けの簡単なWebアプリケーションを作るのに適しています。
WebSiteやWebApplicationを作るための機能を提供し、Webフレームワークを使わない時よりも容易にWebアプリケーションを作ることができるものです。

## Flaskのインストール
pythonのインストールに関しては省きます。

```terminal:terminal
$ pip3 install flask
```
Mac OSの方は、ターミナルを起動し、Windowsの方はコマンドプロンプト(cmd)を起動します。
上記のpipコマンドにてflaskをインストールしてください。
インストールが成功しているかどうかを確認します。

確認するために、Pythonの対話型シェルを起動します。

```terminal:terminal
$ python3
Python 3.7.3 (default, May 21 2019, 16:23:51) 
[Clang 10.0.1 (clang-1001.0.46.3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import flask
>>> flask.__version__
'1.1.2'
```

と表示されれば、Flaskのインストールが完了しています。

# まずは、Hello World!を返してみる


```python:hello.py
from flask import Flask # Flaskのインポート

app = Flask(__name__) # 起動するFlaskアプリケーションを定義

@app.route("/") # @app.route()でルーティング
def hello_world(): # ルーティングされた処理を実行 (helloメソッド)
  return "Hello, World!" # returnで "Hello, World!"を返す

if __name__ == '__main__':
  app.run() # app.run()でアプリケーションを起動
```
ターミナルを開いて、hello.pyを実行してみましょう。

```terminal:terminal
$ python3 hello.py
 * Serving Flask app "hello" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 262-809-242
```

実行するとこのようなメッセージが表示されると思います。

Flaskに備わっているビルドインサーバを利用して起動しているので、開発環境で試すだけにしてくださいという警告が出ています。

それでは、　ブラウザで``http://127.0.0.1:5000/``にアクセスします。

<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/517357/15df7344-486d-2bff-aab9-e3d8fadd16ab.png" width="400px">

上記の通り、``Hello, World!``を返すことができました。
ちなみに、curlで取得を行うと

```terminal:terminal
$ curl http://localhost:5000/
Hello, World!
```
このような形で取得することが可能です。

当然、以下のように複数のルーティングを定義することができます。

```python:home.py
from flask import Flask

app = Flask(__name__) 

@app.route("/") 
def hello_world():
  return "Hello, World!" 

@app.route("/home") # @app.route("/home")でルーティング
def home(): # ルーティングされた処理を実行（homeメソッド)
    return "This is Home page." #returnで "This is Home page."を返す

if __name__ == '__main__':
  app.run()
```

先程と同じように

```
$ python3 home.py
 * Serving Flask app "home" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 262-809-242
```

と実行しましょう。

そして、次は、 ``http://127.0.0.1.5000/home``にアクセスしてみると

<img src ="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/517357/49545d4f-2a14-74ed-46d1-b925f0b95c74.png" width="400px">

上記の通り、``This is Home page.``を返すことができました。
curlでの取得は、

```terminal:terminal
$ curl http://localhost:5000/home
This is Home page.
```
このように取得することができました。

このようにルーティングから処理値の返却程度であれば簡単に実装することが可能です。

# URLを一部引数として受け取る
アクセス時にURLの一部を変数としてルーティング先のメソッドに渡すことができます。

qiitaの記事でも``https://qiita.com/<ユーザ名>``でアクセスすることでそのアカウントのページにアクセスすることができます。
それと同じことをFlaskでも処理することができます。

```python:message.py
from flask import Flask

app = Flask(__name__) 

@app.route('/message/<message>') # @app.route('/message/<message>')でルーティング
def showMessage(message): # ルーティングされた処理を実装（showMessageメソッド)
    return message # returnでmessageに入力された値を返す

if __name__ == '__main__':
  app.run()
```

message.pyを作成します。

上記のように、`パス/<引数>`のようにすると、ルーティングされたメソッドの引数にURLに入力された値を渡すことができます。

```terminal:terminal
$ python3 message.py
 * Serving Flask app "message" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 262-809-242
127.0.0.1 - - [16/Apr/2020 10:25:10] "GET /message/Send%20message HTTP/1.1" 200 -
```
pythonを実行します。

次は、`http://127.0.0.1:5000/message/Send message`にアクセスします。

<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/517357/3d171f31-d25f-84ad-e36e-a8f5d44a9bcd.png" width="400px">

すると、上記のように、message/の後に入力した文字を取得することができます。

curlでの取得は

```terminal:terminal
$ curl http://127.0.0.1ge/Send%20message
Send message
```
* スペースは上記のように表されるため注意してください。

このようにSend messageを取得することができました。

また、URLパラメータに型を指定することもできます。

記法は以下の通りとなります。

```python:int.py
from flask import Flask

app = Flask(__name__) 

@app.route('/messageId/<int:messageId>')
def showMessageId(messageId):
    messages = [
        "zero",
        "one",
        "two",
        "three",
    ]
    return messages[messageId]

if __name__ == '__main__':
  app.run()
```

`http://127.0.0.1:5000/messageId/3`とブラウザ上で検索してみると

<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/517357/a366b124-23b7-bc6a-7f1b-f38607ddbc34.png" width="400px">

このように、`three`と取得することができました。

`http://127.0.0.1:5000/messageId/three`と検索すると、int型ではないため、`Not Found`が返されます。

<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/517357/d508a3f2-270d-dc6b-c826-b80654e8a809.png" width="500px">

int以外にも、以下が利用可能です。

|型|説明|
|:----------|:---------|
|int|整数を受け入れる|
|float|intと同様、浮動小数点を受け入れる|
|path|デフォルト同様だが、スラッシュも受け入れる|

# メソッドで処理を分ける
今度は`GET`と`POST`メソッドで処理を分けてみます。

FlaskでHTTPリクエストメソッドを処理するためには、`request`というパッケージをインポートする必要があります。

```python:method.py
from flask import Flask, request

app = Flask(__name__) 

@app.route('/getRequest', methods=['GET', 'POST'])
def getRequest():
    if request.method == 'POST':
        return request.form['message']
    else:
        return "GET Method"

if __name__ == '__main__':
    app.run()
```

ルーティングの定義の第二引数にメソッドを指定することができます。

以下のような簡単なHTMLを作成してみます。

```html:index.html
<html>
  <head>
    <title>
      Index
    </title>
  </head>
  <body>
    <section>
      <hi>POST</hi>
      <form method="POST" action="http://127.0.0.1:5000/getRequest">
        <input type="text" name="message" />
        <input type="submit" />
      </form>
    </section>
    <section>
      <hi>GET</hi>
      <form method="GET" action="http://127.0.0.1:5000/getRequest">
        <input type="submit" />
      </form>
    </section>
  </body>
</html>
```

index.htmlを作成したら

```terminal:terminal
$ pwd
/Users/takamatsuyuto/Desktop/developer/2020-study/restapi-tutorial
```
を実行します。
そうすることで、今のフォルダの場所をみることができます。

pwdで出力されたフォルダをChromeなどの検索エンジンで検索します。

<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/517357/e9614484-083b-5f9e-078e-50d1120dd608.png" width="600px">

その中から、先程作成したindex.htmlを選択します。
そうすることで、以下のような画面が出力されます。

<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/517357/189359c1-e740-d67c-562d-e8ed9e2ce57b.png" width="400px">

まずはじめに、POSTの欄に何か入力を行います。
試しに、`Send POST`と入力してみます。

<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/517357/edff7dc8-17de-0e4a-72e2-cf39075fb319.png" width="400px">

と先程入力した文字が返って来ると思います。

curlでは

```terminal:terminal
$ curl -X POST -d "message=Send%20message" http://127.0.0.1:5000/getRequest
Send message
```

少し長いですが、このように入力することで、同じように取得することができます。

次に、ページを戻り、GETボタンを押します。

<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/517357/34d40f0e-f81a-8da8-153a-a7e58e70cb98.png" width="400px">

と`GET Method`と返ってきます。

curlでは

```terminal:terminal
$ curl http://127.0.0.1:5000/getRequest
GET Method
```

とすればGET処理をすることができます。

# エラーページを作成してみよう
最後にエラーページのカスタマイズについてです。

Flaskでは何らかエラーが発生した場合に指定したステータスコードとテンプレートページを返すことができます。

まずは、エラーページをカスタマイズするためのpythonを実装します。

```python:error.py
from flask import Flask, render_template

app = Flask(__name__) 

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run()
```
エラーが発生した際に表示するページを作成します。

エラーが発生した際に`render_template`というメソッドを実行してテンプレートとなるファイルを読み込みます。

その際は、`templates`というフォルダの中から対象のファイルを探すため、まず、はじめに、`templates`というフォルダを作成して、その中に、`404.html'を実装してください。

```html:404.html
<html>
  <head>
    <title>
      ページが見つかりません
    </title>
  </head>

  <body>
    <section>
      <div>
        ページが見つかりません。
      </div>
    </section>
  </body>
</html>
```

最後に先程実装した、`error.py`を実行します。

そして、ルーティングされていない、`/hoge`にアクセスしてみます。

<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/517357/ad14a3a3-1ded-b2b5-bde5-e49cd3b94011.png" width="400px">

このようにエラーが出る時には先程作成した、404.htmlが読み込まれます。

curlで実行してみると


```terminal:terminal
 curl http://127.0.0.1:5000/hoge
<html>
  <head>
    <title>
      ページが見つかりません
    </title>
  </head>

  <body>
    <section>
      <div>
        ページが見つかりません。
      </div>
    </section>
  </body>
</html>
```

のように出力されることが確認できます。

# おわりに

今回は、curlの説明や、httpリクエストメソッドなどの説明も簡単に触れつつ、python Flaskで簡単なREST APIを実装してみました。

GETやPUTだけの簡単なAPIであればサックと実装できるという感覚が得られたのではないかと思います。

認証処理などを外部のサービスを利用したりすることを前提にすると、最低限動くレベルのAPIを作ることは難しくはないという印象です。

皆さんもWebサイトを作成する時にバックエンドを実装する際にはREST APIでの実装を一度試してみてください！

以上となります。
