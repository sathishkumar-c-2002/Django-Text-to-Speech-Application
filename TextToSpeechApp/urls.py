# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.text_to_speech, name='text_to_speech'),  # Match the root URL of the app
    path('text-to-speech/', views.text_to_speech, name='text_to_speech'),  # Keep the specific path if needed
]
