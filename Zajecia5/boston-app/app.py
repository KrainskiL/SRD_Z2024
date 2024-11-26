import flask
import pandas as pd
import numpy as np
import pickle
import sklearn

app = flask.Flask(__name__)
model = None


def load_model():
    global model
    with open('Boston_LR.pkl', 'rb') as f:
        model = pickle.load(f)


@app.route("/")
def hello():
    return "This is Boston prediction app. Use <b>/predict</b> endpoint with POST request e.g. <br><br> curl -X POST -F data=@observation.json 'http://localhost:5000/predict'"


@app.route("/predict", methods=["POST"])
def predict():
    data = {"success": False}
    if flask.request.method == "POST":
        if flask.request.files.get("data"):
            observation = pd.read_json(flask.request.files["data"], orient='index').transpose()
            data["prediction"] = model.predict(observation)[0]
            data["success"] = True

    return flask.jsonify(data)


if __name__ == "__main__":
    print("* Loading model and Flask server...")
    load_model()
    app.run(host='0.0.0.0', threaded=False)