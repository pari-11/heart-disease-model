# 🫀 Heart Disease Prediction Web App

This project is a machine learning–powered web application that predicts the risk of heart disease based on user-input medical data. It combines a trained ML model with a Flask backend and a simple HTML interface for user interaction.

---

## 📂 Project Structure

heart-disease-model/  
├── app.py                   # Flask backend to serve predictions  
├── model.pkl                # Trained machine learning model  
├── model_training.ipynb     # Jupyter Notebook used for training and evaluation  
├── requirements.txt         # Python dependencies for the project  
  
├── Templates/               # HTML templates used by Flask  
│   └── index.html           # Main user interface form  
  
├── static/                  # Static assets (images, CSS, JS)  
│   └── bg4.jpg              # Background image for the web app  
│   └── bg2.jpg              # Background image for the web app  

---

## 🚀 How to Run the Project

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/heart-disease-prediction.git
cd heart-disease-prediction
2. (Optional) Create a Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
3. Install the Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Run the Flask App
bash
Copy
Edit
python app.py
5. View the App in Your Browser
Visit http://127.0.0.1:5000/ to use the prediction form.

💡 Features
🧠 Machine learning model built with scikit-learn

🌐 Flask-powered backend

🎨 Simple and clean HTML frontend for inputs

📊 Instant heart disease risk prediction

📌 Requirements
All dependencies are listed in requirements.txt, but key libraries include:

Flask

scikit-learn

pandas

numpy
```
###Author
Parnika Thakur
Student engineer focused on building functional, logic-driven projects.
Comfortable across the full stack — from models to UI, backend to deployment.
