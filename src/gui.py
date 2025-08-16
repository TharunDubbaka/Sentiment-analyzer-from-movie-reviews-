import tkinter as tk
import pickle
from preprocess import clean

model = pickle.load(open("models\\sentiment_model.pkl", "rb"))
vect = pickle.load(open("models\\vectorizer.pkl", "rb"))

def predict():
    text = text_box.get("1.0", tk.END)
    cleaned_text = clean(text)
    vector = vect.transform([cleaned_text])
    proba = model.predict_proba(vector)[0]
    max_prob = max(proba)
    threshold = 0.6
    if max_prob == threshold:
        prediction = "Neutral"
    else:
        prediction = model.classes_[proba.argmax()]
    
    result_label.config(text=f"Sentiment: {prediction}")
root = tk.Tk()
root.title("Sentiment Analyzer")

tk.Label(root, text="Enter your text:", font=("Helvetica", 12)).pack(pady=5)
text_box = tk.Text(root, height=10, width=60, font=("Helvetica", 10))
text_box.pack(pady=5)

tk.Button(root, text="Predict Sentiment", command=predict, font=("Helvetica", 12)).pack(pady=10)
result_label = tk.Label(root, text="Sentiment: ", font=("Helvetica", 12))
result_label.pack(pady=5)

root.mainloop()
