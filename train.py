import pandas as pd
from model import build_autoencoder
from sklearn.preprocessing import StandardScaler

# Load data
data = pd.read_csv("data/creditcard.csv")

X = data.drop("Class", axis=1)
y = data["Class"]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train = X_scaled[y == 0]

# Build model
autoencoder = build_autoencoder(X_train.shape[1])

# Train
autoencoder.fit(X_train, X_train,
                epochs=10,
                batch_size=64,
                shuffle=True)

# Save model
autoencoder.save("model/autoencoder.h5")

# Save scaler
import joblib
joblib.dump(scaler, "model/scaler.pkl")

print("Model saved!")