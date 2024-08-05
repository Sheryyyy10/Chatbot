from django.views import View
from django.http import JsonResponse
from .nlp_utils import preprocess_text
from .intent_classifier import IntentClassifier
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class ChatbotView(View):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_input = request.GET.get('query', '')
        if not user_input:
            return JsonResponse({'error': 'No query provided'}, status=400)

        preprocessed_input = self.preprocess(user_input)
        intent = self.predict_intent(preprocessed_input)

        response = self.generate_response(intent)
        return JsonResponse({'intent': intent, 'response': response})

    def preprocess(self, text):
        return preprocess_text(text)

    def predict_intent(self, text):
        classifier = IntentClassifier()
        return classifier.predict(text)

    def generate_response(self, intent):
        responses = {
                'book_flight': 'I can help you book a flight. Where would you like to go?',
                'weather': 'Sure, let me check the weather for you. Could you tell me your location?',
                'play_music': 'Playing music now. Do you have a specific song or genre in mind?',
                'tell_joke': 'Why don’t scientists trust atoms? Because they make up everything!',
                'get_news': 'Here are the latest news headlines... [news data]',
                'set_timer': 'Setting a timer for 5 minutes. Let me know if you need anything else.'
            }
        return responses.get(intent, "I'm not sure how to help with that.")
