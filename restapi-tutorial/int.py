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
