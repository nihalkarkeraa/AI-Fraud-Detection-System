from flask import Flask, render_template, request, session, redirect, url_for
import numpy as np
import joblib
from tensorflow.keras.models import load_model

app = Flask(__name__)
app.secret_key = "secret123"

# Load model & scaler
model = load_model("model/autoencoder.h5",compile=False)
scaler = joblib.load("model/scaler.pkl")

threshold = 0.25

# Store transactions
transactions = []


# ---------------- LOGIN ----------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        pwd = request.form['password']

        if user == "admin" and pwd == "1234":
            session['user'] = user
            return redirect(url_for('home'))
        else:
            return render_template("login.html", error="Invalid login")

    return render_template("login.html")


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))


# ---------------- HOME ----------------
@app.route('/')
def home():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template("index.html")


# ---------------- PREDICT ----------------
@app.route('/predict', methods=['POST'])
def predict():
    if 'user' not in session:
        return redirect(url_for('login'))

    try:
        amount = float(request.form['amount'])
        time = float(request.form['time'])

        # Generate hidden features
        random_features = np.zeros(28)

        data = np.concatenate(([time], random_features, [amount]))
        data = data.reshape(1, -1)

        # Scale
        data_scaled = scaler.transform(data)

        # Predict
        recon = model.predict(data_scaled)
        error = np.mean((data_scaled - recon) ** 2)
        print("Reconstruction Error:", error)

        risk_score = min(100, error * 1000)

        # Decision
        if error > threshold:
            result = "Fraud Detected 🚨"
            status = "fraud"
        else:
            result = "Safe Transaction ✅"
            status = "safe"

        # Risk level
        if risk_score < 30:
            level = "Low"
        elif risk_score < 70:
            level = "Medium"
        else:
            level = "High"

        # Save transaction
        transactions.append({
            "amount": amount,
            "time": time,
            "risk": round(risk_score, 2),
            "status": result,
            "level": level
        })

        return render_template("index.html",
                               prediction=result,
                               risk=round(risk_score, 2),
                               status=status,
                               level=level)

    except Exception as e:
        return render_template("index.html",
                               prediction="Error in input",
                               risk=0,
                               status="safe",
                               level="Unknown")


# ---------------- DASHBOARD ----------------
@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))

    risks = [t['risk'] for t in transactions]

    return render_template("dashboard.html",
                           data=risks,
                           transactions=transactions)


# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)