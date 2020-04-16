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