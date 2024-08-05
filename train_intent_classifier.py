# chatbot/management/commands/train_intent_classifier.py

from django.core.management.base import BaseCommand
from chat.intent_classifier import IntentClassifier
from chat.nlp_utils import preprocess_text


class Command(BaseCommand):
    help = 'Train the intent classifier'

    def handle(self, *args, **options):
        # Example dataset
        X = [
            "Book a flight", "I need to book a plane ticket", "Help me find a flight",
            "What's the weather like today?", "Tell me the weather", "Is it going to rain?",
            "Play some music", "Can you play a song?", "Start playing music",
            "Tell me a joke", "Make me laugh", "I want to hear a joke",
            "What's the news?", "Give me the latest news", "What's happening in the world?",
            "Set a timer for 5 minutes", "I need a timer for 5 minutes", "Can you set a timer?"
        ]

        y = [
            "book_flight", "book_flight", "book_flight",
            "weather", "weather", "weather",
            "play_music", "play_music", "play_music",
            "tell_joke", "tell_joke", "tell_joke",
            "get_news", "get_news", "get_news",
            "set_timer", "set_timer", "set_timer"
        ]

        X_preprocessed = [preprocess_text(x) for x in X]

        classifier = IntentClassifier()
        classifier.train(X_preprocessed, y)

        self.stdout.write(self.style.SUCCESS('Model trained successfully'))
