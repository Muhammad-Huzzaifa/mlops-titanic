import pandas as pd
import joblib
import os

os.makedirs("results", exist_ok=True)

def predict():
    model = joblib.load("models/model.pkl")
    X_test = pd.read_csv("models/X_test.csv")

    predictions = model.predict(X_test)

    pd.DataFrame(predictions, columns=['Prediction']).to_csv("results/predictions.csv", index=False)

if __name__ == "__main__":
    predict()
    print("Predictions made and saved to results/predictions.csv")
