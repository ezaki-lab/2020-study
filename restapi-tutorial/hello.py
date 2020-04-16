from flask import Flask # Flaskのインポート

app = Flask(__name__) # 起動するFlaskアプリケーションを定義

@app.route("/") # @app.route()でルーティング
def hello_world(): # ルーティングされた処理を実行 (helloメソッド)
  return "Hello, World!" # returnで "Hello, World!"を返す

if __name__ == '__main__':
  app.run() # app.run()でアプリケーションを起動