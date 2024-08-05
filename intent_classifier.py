
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import joblib


class IntentClassifier:
    def __init__(self):
        self.vectorizer = CountVectorizer()
        self.classifier = LogisticRegression()

    def train(self, X, y):
        X_vec = self.vectorizer.fit_transform(X)
        self.classifier.fit(X_vec, y)
        joblib.dump((self.vectorizer, self.classifier), 'intent_model.pkl')

    def predict(self, text):
        vectorizer, classifier = joblib.load('intent_model.pkl')
        X_vec = vectorizer.transform([text])
        return classifier.predict(X_vec)[0]
