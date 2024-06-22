from flask import Flask, jsonify, request
from train import testpypy, testpypy2
# from flask_talisman import Talisman
from flask_cors import CORS, cross_origin


app = Flask(__name__)
# Talisman(app)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
def home():
    return "Hello, Flask with HTTPS!"

# Water Level Prediction
@app.route('/predict', methods=['POST'])
@cross_origin()
def create_date():
    if not request.json or not 'day' in request.json:
        return jsonify({"error": "Bad Request"}), 400
    
    if not request.json or not 'month' in request.json:
        return jsonify({"error": "Bad Request"}), 400
    res = testpypy(request.json['day'], request.json["month"])
    predict = {
        "siwak": res[1],
        "bintang_ninggi": res[0]
    }
    return jsonify(predict), 201

# Water Level Prediction
@app.route('/model-2/predict', methods=['POST'])
def create_predict():
    if not request.json or not 'day' in request.json:
        return jsonify({"error": "Bad Request"}), 400
    
    if not request.json or not 'month' in request.json:
        return jsonify({"error": "Bad Request"}), 400
    res = testpypy2(request.json['day'], request.json["month"])
    predict = {
        "siwak": res[1],
        "bintang_ninggi": res[0]
    }
    return jsonify(predict), 201

if __name__ == '__main__':
    # app.run(debug=True, ssl_context=("cert.pem", "key.pem"))
    app.run(debug=True)
