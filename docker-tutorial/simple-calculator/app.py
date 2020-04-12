from flask import Flask
from flask import jsonify
from flask import request


app = Flask(__name__)

@app.route("/")
def hello():
    return "Simple calculator"

@app.route('/sum', methods=['POST'])
def sum():
    # ポストされたJSONを取得
    request_json = request.json
    numbers = request_json['values']
    # 合計を計算
    result = 0
    for num in numbers:
        result += num
    # 返信
    return jsonify({'result': result})

@app.route('/max', methods=['POST'])
def max():
    # ポストされたJSONを取得
    request_json = request.json
    numbers = request_json['values']
    # 最大値を計算
    result = 0
    for num in numbers:
        if num > result:
            result = num
    # 返信
    return jsonify({'result': result})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)