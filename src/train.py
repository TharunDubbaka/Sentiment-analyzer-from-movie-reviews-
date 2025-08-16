import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
import pickle
from preprocess import clean

df = pd.read_csv("C://Users//dubba//OneDrive//Desktop//Major projects//Sentiment analyser with RNN//data//reviews.csv") 
df['cleaned'] = df['text'].apply(clean)
vect = TfidfVectorizer(max_features=3000)
X = vect.fit_transform(df['cleaned'])
y = df['sentiment']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = MultinomialNB()
model.fit(X_train, y_train)
pickle.dump(model, open("models\\sentiment_model.pkl", "wb"))
pickle.dump(vect, open("models\\vectorizer.pkl", "wb"))
print("Model and vectorizer saved successfully!")
