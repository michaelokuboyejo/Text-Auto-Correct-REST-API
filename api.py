from flask import Flask, jsonify

from index import AutoCorrect

app = Flask(__name__)

auto_correct = AutoCorrect()


@app.route('/', methods=['GET'])
def index():
    return jsonify({'status': 'ok'})


@app.route('/predict/<word>', methods=['GET'])
def predict(word: str):
    return jsonify(auto_correct.check(word))


if __name__ == '__main__':
    app.run(debug=True)
