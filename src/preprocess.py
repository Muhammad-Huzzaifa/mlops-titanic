import pandas as pd
import os

os.makedirs("data/processed", exist_ok=True)

def preprocess_data():
    df = pd.read_csv("data/raw/titanic.csv")

    # Handle missing values
    df['Age'].fillna(df['Age'].median(), inplace=True)
    df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

    # Encode categorical variables
    df['Sex'] = df['Sex'].map({'female': 0, 'male': 1})
    df = pd.get_dummies(df, columns=['Embarked'], drop_first=True)

    df.to_csv("data/processed/processed.csv", index=False)

if __name__ == "__main__":
    preprocess_data()
    print("Data preprocessed and saved to data/processed/processed.csv")
