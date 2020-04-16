from flask import Flask

app = Flask(__name__) 

@app.route('/message/<message>') # @app.route('/message/<message>')でルーティング
def showMessage(message): # ルーティングされた処理を実装（showMessageメソッド)
    return message # returnでmessageに入力された値を返す

if __name__ == '__main__':
  app.run()