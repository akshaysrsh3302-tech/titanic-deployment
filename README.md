# Titanic Survival Predictor

A Machine Learning web application that predicts whether a passenger would have survived the Titanic disaster based on features like gender, age, passenger class, fare, title, and family size.

The model is built using Random Forest and deployed as an interactive web app on Render.com.

---

## 🚀 Live Demo

**Live URL:** [https://titanic-survival-tvyy.onrender.com]

---

## ✨ Features

- Easy-to-use web form for passenger details
- Instant survival prediction with probability percentage
- Clean and responsive interface
- Smart feature engineering (Title, Family Size, Has Cabin, etc.)

---

## 📊 Model Performance

- **Best Model**: Random Forest  
- **Test Accuracy**: ~82%  
- **Key Features**: Sex, Title, Pclass, Fare, Age  

The model correctly reflects historical patterns — women, children, and higher-class passengers had much better survival chances.

---

## 🌐 Deployment on Render

This project is successfully deployed on **Render.com** (Free Tier).

### Deployment Settings Used:
- **Runtime**: Python  
- **Build Command**: `pip install -r requirements.txt`  
- **Start Command**: `gunicorn app:app`

> **Note**: On free tier, the app may take 30–60 seconds to wake up (cold start) after inactivity.

---

## 🚀 How to Run Locally

### Prerequisites
- Python 3.9 or higher

### Steps

1. Clone the repository
   ```bash
   git clone https://github.com/akshaysrsh3302-tech/titanic-deployment.git
   cd titanic-deployment

2. Install dependencies
   ```bash
   pip install -r requirements.txt

3. Run the application
   ```bash
   python app.py

4. Open your browser and go to http://127.0.0.1:5000
