# Titanic Survival Predictor

A complete Machine Learning web application that predicts whether a passenger would have survived the Titanic disaster. The model is trained on the classic Titanic dataset and deployed as an interactive web app.

---

## 🚀 Live Demo

**🔗 Live URL:** https://titanic-survival-tvyy.onrender.com

Enter passenger details and get instant survival predictions!

---

## ✨ Features

- Predict survival chances based on real historical features
- Clean and easy-to-use web interface
- Shows survival prediction along with probability percentage
- Fully deployed and accessible online

---

## 🛠️ Tech Stack

- **Machine Learning**: Scikit-learn (Random Forest), Pandas, NumPy
- **Backend**: FastAPI / Flask
- **Frontend**: HTML + CSS (Jinja2 templates)
- **Deployment**: Render.com
- **Model Saving**: Joblib

---

## 🌐 Deployment on Render

This project is successfully deployed on **Render.com** (Free tier).

### Deployment Settings Used:

- **Runtime**: Python  
- **Build Command**: `pip install -r requirements.txt`  
- **Start Command**: `gunicorn app:app`

> **Note**: On the free tier, the app may take 30–60 seconds to wake up from sleep (cold start) when you first visit the link.

---

## 📊 Model Performance

- **Best Model**: Random Forest  
- **Test Accuracy**: ~82%  
- **Key Features**: Sex, Title, Pclass, Fare, Age  

The model correctly captures historical patterns — women and children in higher classes had significantly better survival rates.

---

## 🚀 How to Run Locally

### Prerequisites
- Python 3.9+

### Steps

1. Clone the repository
   ```bash
   git clone https://github.com/YOUR-USERNAME/titanic-deployment.git
   cd titanic-deployment
