from django.urls import path
from .views import *

urlpatterns = [
    path('', ContactForm, name="contact-form"),
    # path('', ContactUs.as_view(), name="contact-form")
]