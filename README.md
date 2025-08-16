# Sentiment-analyzer-from-movie-reviews-
A Sentiment Analysis project using TF-IDF and Naive Bayes to classify text as positive or negative. It Includes data preprocessing,feature extraction,model training,and saved models for easy reuse.
This project is a Sentiment Analysis system that classifies text reviews as Positive or Negative.
It uses TF-IDF (Term Frequency–Inverse Document Frequency) for feature extraction and a Naive Bayes classifier for prediction.

Features : 

Text preprocessing (cleaning raw reviews).

TF-IDF vectorization with 3000 features.

Naive Bayes model for fast and accurate classification.

Saves both the trained model and vectorizer for reuse.

Installation :

Clone the repo and install dependencies:

git clone https://github.com/yourusername/sentiment-analysis-tfidf.git
cd sentiment-analysis-tfidf
pip install -r requirements.txt

Train the model
python train.py

 Saves model and vectorizer inside models/.

Test predictions
python predict.py


Example output:

"I loved this movie, it was amazing!" → Positive  
"This product is terrible and boring." → Negative  

 Skills Demonstrated :

Data Cleaning & Preprocessing

Feature Engineering with TF-IDF

Machine Learning (Naive Bayes)

Model Saving & Loading

GitHub Project Structuring

Future Improvements :

Add a neutral sentiment class.

Extend to deep learning models (RNN/LSTM/BERT).

Deploy as a Flask/Streamlit web app for live demo.

License :

This project is open-source under the MIT License.
