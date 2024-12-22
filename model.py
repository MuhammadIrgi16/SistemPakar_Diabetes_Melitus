import pandas as pd

dataset = pd.read_csv('diabetes.csv')

def diagnosa(patient_data):
    if patient_data['Glucose'] > 120:
        return "Glukosa tinggi, kemungkinan diabetes."

    if patient_data['BMI'] > 30 and patient_data['Age'] > 45:
        return "BMI dan umur diatas 45 tahun, resiko tinggi diabetes."

    if patient_data['BloodPressure'] > 80 and patient_data['Insulin'] < 30:
        return "Tekanan darah tinggi and insulin level rendah, potensi beresiko diabetes."

    if patient_data['DiabetesPedigreeFunction'] > 0.5:
        return "Memiliki genetik diabetes, resiko lebih tinggi."

    if patient_data['Pregnancies'] > 3 and patient_data['Glucose'] > 120:
        return "History of gestational diabetes, high risk."

    if patient_data['Age'] > 60 and patient_data['BMI'] > 30:
        return "Umur diatas 60 tahundan BMI diatas 30, beresiko diabetes."

    if patient_data['Insulin'] < 30 and patient_data['SkinThickness'] > 25:
        return "Insulin rendah dan ketebalan kulit tinggi, masalah metabolisme beresiko diabetes."

    if patient_data['Age'] > 50 and patient_data['Glucose'] > 150:
        return "Tinggi glukosa dan umur diatas 50 tahun, beresiko tinggi terkena diabetes."

    return "Tidak ada resiko terkena diabetes dari hasil."
