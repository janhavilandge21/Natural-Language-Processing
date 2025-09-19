

# NLP Playground with NLTK
A simple, beginner-friendly repository demonstrating common Natural Language Processing tasks using NLTK (tokenization, stemming/lemmatization, stopword removal, POS tagging, TF-IDF, basic text classification, and visualization). This README is based on the project notes in the uploaded NLTK.pdf. 


Project Overview

This repository is an interactive NLP Playground built with Python and NLTK to help learners explore and experiment with essential NLP building blocks. It is intended for students and beginner practitioners who want runnable examples and explanations for text preprocessing, classical feature extraction, and simple ML pipelines.

(See NLTK.pdf for detailed explanations and notes). 

NLTK

Features

Text cleaning & normalization (lowercasing, punctuation removal)

Tokenization (word & sentence)

Stopword removal

Stemming (Porter) and Lemmatization

POS tagging and chunking examples

TF-IDF vectorization and naive classifiers

Example pipelines for sentiment / topic-style classification

Small visualization examples (word frequency, n-grams)

Jupyter notebooks with step-by-step explanations

Quick Demo

After installing dependencies, run the included notebooks or scripts to:

Tokenize a sample document into sentences and words

Compare PorterStemmer vs WordNetLemmatizer outputs

Train a simple Naive Bayes classifier on sample data

View top-n frequent words and n-grams

Installation



(Recommended) Create a virtual environment:

python -m venv .venv
source .venv/bin/activate    # macOS / Linux
.venv\Scripts\activate       # Windows


Install dependencies:

pip install -r requirements.txt


Download NLTK data (run once):

python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet'); nltk.download('averaged_perceptron_tagger')"

Usage
Run Jupyter Notebook (interactive)
jupyter notebook
# open notebooks/00-intro-nltk.ipynb

Run example script
python scripts/run_app.py


Example snippet (tokenize + stemming):

from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

text = "NLTK makes natural language processing with Python straightforward and fun."
tokens = word_tokenize(text)
pst = PorterStemmer()
stems = [pst.stem(t) for t in tokens if t.isalpha()]
print(stems)



Data

The data/ folder contains small sample files for demos (CSV or TXT). This repo is designed for educational purposes; replace or extend with real datasets for experiments.

See data/README.md for the format and instructions.

Requirements

Example requirements.txt (pin versions if needed):

nltk>=3.5
scikit-learn>=1.0
pandas
matplotlib
jupyter


Install using:

pip install -r requirements.txt


(Adjust versions according to your environment; the notebooks are tested with Python 3.8+.)

Tests

There are small smoke-test scripts in scripts/ to verify imports and basic processing. Run:

python scripts/run_smoke_tests.py

