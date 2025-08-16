# Sentiment Analysis with TF-IDF + Naive Bayes

This project is a Sentiment Analysis system that classifies text reviews as Positive or Negative.
It uses TF-IDF (Term Frequency–Inverse Document Frequency) for feature extraction and a Naive Bayes classifier for prediction.

# Features:

Text preprocessing (cleaning raw reviews).

TF-IDF vectorization with 3000 features.

Naive Bayes model for fast and accurate classification.

Saves both the trained model and vectorizer for reuse.

# Project Structure:

data/ → contains dataset (reviews.csv or sample data)

models/ → stores saved models (.pkl files)

preprocess.py → text cleaning functions

train.py → training script

predict.py → (optional) script to test predictions

requirements.txt → project dependencies

README.md → documentation

.gitignore → ignored files

# Installation:

Clone the repository

Go into the project folder

Install dependencies from requirements.txt

# Usage:

Run train.py to train the model (saves model and vectorizer into models/).

Run predict.py to test predictions.

# Example output:

"I loved this movie, it was amazing!" → Positive

"This product is terrible and boring." → Negative

# Skills Demonstrated:

Data Cleaning and Preprocessing

Feature Engineering with TF-IDF

Machine Learning (Naive Bayes)

Model Saving and Loading

GitHub Project Structuring

# Future Improvements:

Add a neutral sentiment class.

Extend to deep learning models (RNN/LSTM/BERT).

Deploy as a Flask or Streamlit web app for live demo.

# License:
This project is open-source under the MIT License.
