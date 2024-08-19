from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

app = Flask(__name__)

# Load the model and LabelEncoder
# Load the model and encoder
with open('model/model_rf.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('model/label_encoder.pkl', 'rb') as encoder_file:
    encoder = pickle.load(encoder_file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve form data
    N = float(request.form['N'])
    P = float(request.form['P'])
    K = float(request.form['K'])
    temperature = float(request.form['temperature'])
    humidity = float(request.form['humidity'])
    ph = float(request.form['ph'])
    rainfall = float(request.form['rainfall'])
    
    # Prepare the input data for prediction
    input_data = pd.DataFrame([[N, P, K, temperature, humidity, ph, rainfall]], 
                              columns=['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall'])
    
    # Make prediction
    encoded_prediction = model.predict(input_data)
    original_prediction = encoder.inverse_transform(encoded_prediction)[0]
    
    # Return the result as JSON
    return jsonify({'prediction': original_prediction})

if __name__ == '__main__':
    app.run(debug=True)
