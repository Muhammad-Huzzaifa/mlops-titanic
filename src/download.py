import pandas as pd
import os

os.makedirs("data/raw", exist_ok=True)

def download_data():
    url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    df = pd.read_csv(url)
    df.to_csv("data/raw/titanic.csv", index=False)

if __name__ == "__main__":
    download_data()
    print("Data downloaded and saved to data/raw/titanic.csv")
