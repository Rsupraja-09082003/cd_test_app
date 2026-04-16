from flask import Flask, request, jsonify  
import pickle  
import numpy as np  

app = Flask(__name__)

# load model (you will add this later) 
# model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return "ML Model is running lets goooo!" 

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json["data"] 

    # convert input
    input_array = np.array(data).reshape(1, -1)

    # prediction (dummy for now)
    prediction = sum(data)  # replace with model.predict

    return jsonify({
        "prediction": prediction
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000) 
    
