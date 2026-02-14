import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def evaluate():
    y_test = pd.read_csv("models/y_test.csv")
    predictions = pd.read_csv("results/predictions.csv")

    accuracy = accuracy_score(y_test, predictions)
    precision = precision_score(y_test, predictions)
    recall = recall_score(y_test, predictions)
    f1 = f1_score(y_test, predictions)

    with open("results/metrics.txt", "w") as f:
        f.write(f"Accuracy: {accuracy}\n")
        f.write(f"Precision: {precision}\n")
        f.write(f"Recall: {recall}\n")
        f.write(f"F1 Score: {f1}\n")

if __name__ == "__main__":
    evaluate()
    print("Evaluation completed and metrics saved to results/metrics.txt")
