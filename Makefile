PYTHON=python3

setup:
	pip install -r requirements.txt

data/raw/titanic.csv: src/download.py
	$(PYTHON) src/download.py

data/processed/processed.csv: data/raw/titanic.csv src/preprocess.py
	$(PYTHON) src/preprocess.py

features/features.csv: data/processed/processed.csv src/features.py
	$(PYTHON) src/features.py

models/model.pkl: features/features.csv src/train.py
	$(PYTHON) src/train.py

results/predictions.csv: models/model.pkl models/X_test.csv src/predict.py
	$(PYTHON) src/predict.py

results/metrics.txt: results/predictions.csv models/y_test.csv src/evaluate.py
	$(PYTHON) src/evaluate.py

all: results/metrics.txt

clean:
	rm -rf data/processed/*
	rm -rf data/raw/*
	rm -rf features/*
	rm -rf models/*
	rm -rf results/*
