import flask
import pandas as pd
import numpy as np
import pickle

app = flask.Flask(__name__)
model = None


def load_models():
    global model_lr
    with open('Boston_LR.pkl', 'rb') as f:
        model_lr = pickle.load(f)
    global model_dtr
    with open('Boston_DTR.pkl', 'rb') as f:
        model_dtr = pickle.load(f)
    global model_btr
    with open('Boston_BTR.pkl', 'rb') as f:
        model_btr = pickle.load(f)


@app.route("/")
def hello():
    return """This is Boston prediction app. Use <b>/predict</b> endpoint with POST request e.g. <br><br>
    curl -X POST -F data=@house.json 'http://localhost:5000/predict'"""


@app.route("/predict", methods=["POST"])
def predict():
    epsilon = 0.8
    bandits = [("Boosted Trees", model_btr),
        ("Linear Regression", model_lr),
        ("Decision Tree", model_dtr)]
    pick_probs = np.arange(epsilon,1.0001,(1-epsilon)/(len(bandits)-1))
    pick = np.random.rand()
    index = sum([e < pick for e in pick_probs])
    model_name, model = bandits[index]
    data = {"success": False}
    if flask.request.method == "POST":
        if flask.request.files.get("data"):
            observation = pd.read_json(flask.request.files["data"], orient='index').transpose()
            data["prediction"] = model.predict(observation)[0]
            data["model"] = model_name
            data["success"] = True

    return flask.jsonify(data)


if __name__ == "__main__":
    print("* Loading models and Flask server...")
    load_models()
    app.run(host='0.0.0.0', threaded=False)
