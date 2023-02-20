from django.urls import path
from .views import *


urlpatterns = [
    path('reviews/', return_feedback, name='return_feedback'),
]
