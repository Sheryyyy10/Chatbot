from django.urls import path
from .views import *

urlpatterns = [
    path('query/', ChatbotView.as_view(), name='handle_query'),
]
