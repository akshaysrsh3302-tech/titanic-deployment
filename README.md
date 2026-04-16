# Titanic Survival Predictor

A complete Machine Learning web application that predicts whether a passenger would have survived the Titanic disaster based on key features like gender, age, passenger class, fare, and more.

The model is trained on the famous Titanic dataset and deployed as a user-friendly web app using **FastAPI** and hosted on **Render**.

---

## 🚀 Live Demo

The application is live and ready to use:

**🔗 Live URL:** `https://titanic-survival-tvyy.onrender.com`

Try it out by entering passenger details and getting instant survival predictions!

---

## ✨ Project Highlights

- **Accurate Prediction Model**: Built using Random Forest with smart feature engineering (Title extraction, Family Size, Has Cabin, etc.)
- **Interactive Web Interface**: Clean and intuitive form to input passenger information
- **Real-time Results**: Shows survival prediction along with probability percentage
- **Deployed on Render**: Fully hosted and accessible from anywhere
- **Educational & Practical**: Great example of end-to-end ML model deployment

---

## 🛠️ Tech Stack

- **Machine Learning**: Scikit-learn (Random Forest), Pandas, NumPy
- **Backend**: FastAPI
- **Frontend**: Simple HTML + CSS (with Jinja2 templates)
- **Deployment**: Render.com
- **Model Saving**: Joblib

---

## 📋 Features

- Predict survival chances based on real Titanic passenger attributes
- Clean and responsive web interface
- Displays survival probability for better interpretation
- Easy to test different scenarios (e.g., 1st class female vs 3rd class male)

---

## 🚀 How to Run Locally

### Prerequisites
- Python 3.9 or higher

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR-USERNAME/titanic-deployment.git
   cd titanic-deployment


##🌐 Deployment on Render
This project is successfully deployed on Render.com (Free tier).
Deployment Settings Used:

Runtime: Python
Build Command: pip install -r requirements.txt
Start Command: gunicorn app:app

The app wakes up automatically when you visit the link (may take 30–60 seconds on free tier due to cold start).

##📊 Model Performance

Best Model: Random Forest
Test Accuracy: ~82%
Key Features: Sex, Title, Pclass, Fare, Age

The model correctly captures historical patterns — women and children in higher classes had significantly better survival rates.
