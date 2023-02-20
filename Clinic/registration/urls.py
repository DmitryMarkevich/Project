from django.urls import path
from .views import *

urlpatterns = [
    path('registration/', new_registration, name='new_registration'),
    path('registrants/', get_registrants, name='get_registrants'),
    path('registrants_detail_day/', get_registrants_detail, name='registrants_detail_day'),
    path('registrants_detail_month/', get_registrants_detail, name='registrants_detail_month'),
]
