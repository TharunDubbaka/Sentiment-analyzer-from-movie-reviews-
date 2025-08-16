import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import nltk
nltk.download('stopwords')

sw = set(stopwords.words('english'))
ps = PorterStemmer()

def clean(text):
    text = text.lower()
    text = "".join([ch for ch in text if ch not in string.punctuation])
    words = text.split()
    words = [ps.stem(word) for word in words if word not in sw]
    return " ".join(words)
