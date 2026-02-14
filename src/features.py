import pandas as pd
import os

os.makedirs("features", exist_ok=True)

def features_engineering():
    df = pd.read_csv("data/processed/processed.csv")

    # Create new features
    df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
    df['IsAlone'] = (df['FamilySize'] == 1).astype(int)

    # Drop unnecessary columns
    df = df.drop(columns=['PassengerId', 'Name', 'SibSp', 'Parch', 'Ticket', 'Cabin'])

    df.to_csv("features/features.csv", index=False)

if __name__ == "__main__":
    features_engineering()
    print("Features created and saved to features/features.csv")
