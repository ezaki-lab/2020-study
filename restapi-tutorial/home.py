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