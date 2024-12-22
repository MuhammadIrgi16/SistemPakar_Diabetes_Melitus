from flask import Flask, render_template, request
import pandas as pd
from model import diagnosa

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/diagnosa', methods=['POST'])
def diagnosa_user():
    glucose = float(request.form['glucose'])
    bmi = float(request.form['bmi'])
    blood_pressure = float(request.form['blood_pressure'])
    insulin = float(request.form['insulin'])
    age = int(request.form['age'])
    pregnancies = int(request.form['pregnancies'])
    diabetes_pedigree_function = float(request.form['diabetes_pedigree_function'])
    skin_thickness = float(request.form['skin_thickness'])
    
    patient_data = {
        'Pregnancies': pregnancies,
        'Glucose': glucose,
        'BloodPressure': blood_pressure,
        'SkinThickness': skin_thickness,
        'Insulin': insulin,
        'BMI': bmi,
        'DiabetesPedigreeFunction': diabetes_pedigree_function,
        'Age': age
    }
    
    result = diagnosa(patient_data)
    
    return render_template('result.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
