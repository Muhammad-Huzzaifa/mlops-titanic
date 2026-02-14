# Titanic MLOps Pipeline (Automation with Makefile)

This project implements an **end-to-end Machine Learning pipeline** using the Titanic Survival dataset.
The entire workflow is automated using **GNU Make**, allowing the project to be executed with a single command while ensuring reproducibility and proper dependency tracking.

Instead of manually running scripts, the pipeline is built as a **file-based dependency graph**.
Each stage produces artifacts that are required by the next stage, enabling incremental execution (only outdated steps rerun).

---

## Project Structure

```
mlops-titanic/
│
├── Makefile                 # Central pipeline controller
├── requirements.txt         # Python dependencies
├── README.md
│
├── data/
│   ├── raw/                 # Downloaded dataset (auto generated)
│   └── processed/           # Cleaned dataset
│
├── features/                # Feature engineered dataset
│
├── models/                  # Trained model and test split
│
├── results/                 # Predictions and evaluation metrics
│
├── src/
│   ├── download.py          # Downloads Titanic dataset
│   ├── preprocess.py        # Cleans and encodes data
│   ├── features.py          # Feature engineering
│   ├── train.py             # Model training (Random Forest)
│   ├── predict.py           # Generate predictions
│   └── evaluate.py          # Compute metrics
```

---

## Pipeline Workflow

The pipeline follows this dependency chain:

```
Download Data
      ↓
Preprocess Data
      ↓
Feature Engineering
      ↓
Train Model
      ↓
Predict
      ↓
Evaluate
```

Each step only runs if its input files change, ensuring reproducibility and efficient execution.

---

## Installation & Usage

### 1. Clone the repository

```
git clone <repo-url>
cd mlops-titanic
```

### 2. Run the complete pipeline

```
make setup (only needed once to install dependencies)
make all
```

This will automatically:

* Install dependencies
* Download the dataset
* Preprocess data
* Create features
* Train the model
* Generate predictions
* Evaluate performance

---

## Other Useful Commands

Run a specific stage:

```
make data/raw/titanic.csv
make data/processed/processed.csv
make features/features.csv
make models/model.pkl
make results/predictions.csv
make results/metrics.txt
```

Clean generated files:

```
make clean
```

---

## Output Artifacts

After execution:

| File                         | Description                     |
| ---------------------------- | ------------------------------- |
| data/raw/titanic.csv         | Downloaded dataset              |
| data/processed/processed.csv | Clean dataset                   |
| features/features.csv        | Feature engineered dataset      |
| models/model.pkl             | Trained model                   |
| results/predictions.csv      | Model predictions               |
| results/metrics.txt          | Accuracy, Precision, Recall, F1 |

---

## Key Concepts Demonstrated

* Reproducible ML pipelines
* Automation using GNU Make
* File-based dependency tracking
* Incremental execution (only rerun outdated steps)
* Production-style ML workflow

---

## Running on a Fresh System

The project is designed to run on a clean machine:

```
git clone <repo>
cd mlops-titanic
make setup
make all
```

No manual steps required.

---
**Name:** Muhammad Huzaifa

**Roll Number:** 23F-0043
