import pandas as pd
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

os.makedirs("models", exist_ok=True)

def train_model():
    df = pd.read_csv("features/features.csv")

    X = df.drop(columns=['Survived'])
    y = df['Survived']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    joblib.dump(model, "models/model.pkl")
    X_test.to_csv("models/X_test.csv", index=False)
    y_test.to_csv("models/y_test.csv", index=False)

if __name__ == "__main__":
    train_model()
    print("Model trained and saved to models/model.pkl")
