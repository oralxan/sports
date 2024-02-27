# urls.py

from django.urls import path
from .views import ContactMessageAPIView

urlpatterns = [
    path('contact/', ContactMessageAPIView.as_view(), name='contact-message'),
]
