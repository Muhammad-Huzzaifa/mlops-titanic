PYTHON=python3

setup:
	pip install -r requirements.txt

download-data:
	$(PYTHON) src/download.py

preprocess:
	$(PYTHON) src/preprocess.py

features:
	$(PYTHON) src/features.py

train:
	$(PYTHON) src/train.py

predict:
	$(PYTHON) src/predict.py

evaluate:
	$(PYTHON) src/evaluate.py

all: download-data preprocess features train predict evaluate

clean:
	rm -rf data/processed/*
	rm -rf data/raw/*
	rm -rf features/*
	rm -rf models/*
	rm -rf results/*
