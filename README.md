# Overview

This Django-based chatbot application is designed to interact with users through a natural language interface. The chatbot can understand user queries, classify the intent behind the query, and respond accordingly. It utilizes natural language processing (NLP) for preprocessing text and predicting intents. The application also includes token-based authentication and permission classes to ensure that only authenticated users can access the chatbot services.

# Features

Intent Classification: The chatbot can classify user intents such as booking a flight, checking the weather, playing music, telling jokes, fetching news, and setting timers.
Token Authentication: Only authenticated users can interact with the chatbot, ensuring secure access.
Preprocessing: User inputs are preprocessed for better intent classification.
Response Generation: The chatbot generates appropriate responses based on the predicted intent.
Setup and Installation
Prerequisites
Python 3.7+
Django 3.0+
Django REST Framework
Additional libraries: requests, nltk (for NLP), etc.

# Libraries and Package 

scikit-learn: For text vectorization and logistic regression model.
nltk: For text preprocessing, including stopwords removal and lemmatization.
spacy: For advanced NLP tasks (e.g., tokenization).
joblib: For saving and loading trained models.

# Parameters:

query: The user's query as a string.

# Response:

intent: The predicted intent of the user's query.
response: The chatbot's response based on the predicted intent.


# Code Structure

views.py: Contains the ChatbotView class which handles GET requests.
nlp_utils.py: Contains the preprocess_text function for text preprocessing.
intent_classifier.py: Contains the IntentClassifier class responsible for predicting user intents.
settings.py: Contains the Django settings, including REST framework configurations.

This application uses token-based authentication to ensure that only authorized users can access the chatbot. Users must provide a valid token in their requests to interact with the chatbot.
