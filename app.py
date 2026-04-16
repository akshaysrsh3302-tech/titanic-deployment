from flask import Flask, request, render_template
import joblib
import pandas as pd
import os

app = Flask(__name__)

# Load model
try:
    model = joblib.load('titanic_survival_model.pkl')
    print("✅ Model loaded successfully")
except Exception as e:
    print(f"❌ Error loading model: {e}")
    model = None

# Load feature columns if available
try:
    feature_columns = joblib.load('feature_columns.pkl')
    print("✅ Feature columns loaded")
except:
    feature_columns = None
    print("⚠️ Feature columns not found")

# Mapping (must match your training)
sex_map = {'male': 1, 'female': 0}
embarked_map = {'C': 0, 'Q': 1, 'S': 2}
title_map = {'Mr': 0, 'Miss': 1, 'Mrs': 2, 'Master': 3, 'Rare': 4}

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if model is None:
            return "Model failed to load. Check Render logs.", 500

        try:
            data = {
                'Pclass': int(request.form['Pclass']),
                'Sex': request.form['Sex'],
                'Age': float(request.form['Age']),
                'SibSp': int(request.form['SibSp']),
                'Parch': int(request.form['Parch']),
                'Fare': float(request.form['Fare']),
                'Embarked': request.form['Embarked'],
                'Title': request.form.get('Title', 'Mr'),
                'Has_Cabin': int(request.form.get('Has_Cabin', 0)),
                'FamilySize': int(request.form.get('FamilySize', 1)),
                'IsAlone': int(request.form.get('IsAlone', 1))
            }

            input_df = pd.DataFrame([data])

            # Encoding
            input_df['Sex'] = input_df['Sex'].map(sex_map)
            input_df['Embarked'] = input_df['Embarked'].map(embarked_map)
            input_df['Title'] = input_df['Title'].map(title_map)

            if feature_columns:
                input_df = input_df.reindex(columns=feature_columns, fill_value=0)

            prediction = model.predict(input_df)[0]
            probability = round(model.predict_proba(input_df)[0][1] * 100, 2)

            result = "✅ Survived" if prediction == 1 else "❌ Did Not Survive"

            return render_template('index.html', prediction=result, probability=probability)

        except Exception as e:
            return f"Error: {str(e)}", 400

    return render_template('index.html', prediction=None)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
