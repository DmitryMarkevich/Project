from django.urls import path, include
from rest_framework import routers

from .yasg import urlpatterns as swag_urls

from .views import *
from .api_views import *
from reviews.api_views import ReviewsAPIView

router = routers.DefaultRouter()

router.register(r'employee', EmployeeAPIView)
router.register(r'service', ServiceAPIView)
router.register(r'professions', ProfessionsAPIView)
router.register(r'client', ClientAPIView)
router.register(r'reviews', ReviewsAPIView)


urlpatterns = [
    path('clinic/', clinic, name='clinic'),
    path('services/', services, name='services'),
    path('detailed_services/<int:pk>/', detailed_services, name='detailed_services'),
    path('prices/', prices, name='prices'),
    path('contacts/', all_contacts, name='contacts'),
    path('our_specialists/', our_specialists, name='our_specialists'),
    path('detailed_by_specialist/<int:pk>/', detailed_by_specialist, name='detailed_by_specialist'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]

urlpatterns += swag_urls
