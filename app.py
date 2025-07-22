from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open('model1.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # HTML form for input

@app.route('/predict', methods=['POST'])
def predict():
    # Fetch input values from form
    age = float(request.form.get('age'))
    anaemia = float(request.form.get('anaemia'))
    creatinine_phosphokinase = float(request.form.get('creatinine_phosphokinase'))
    diabetes = float(request.form.get('diabetes'))
    ejection_fraction = float(request.form.get('ejection_fraction'))
    high_blood_pressure = float(request.form.get('high_blood_pressure'))
    platelets = float(request.form.get('platelets'))
    serum_creatinine = float(request.form.get('serum_creatinine'))
    serum_sodium = float(request.form.get('serum_sodium'))
    sex = float(request.form.get('sex'))
    smoking = float(request.form.get('smoking'))
    time = float(request.form.get('time'))

    # Prepare features for prediction
    features = np.array([
        age, anaemia, creatinine_phosphokinase, diabetes, ejection_fraction,
        high_blood_pressure, platelets, serum_creatinine, serum_sodium,
        sex, smoking, time
    ]).reshape(1, -1)

    # Predict using model
    prediction = model.predict(features)[0]

    result = "High Risk of Death" if prediction == 1 else "Low Risk of Death"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
