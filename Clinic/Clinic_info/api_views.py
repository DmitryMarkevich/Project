from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Employee, Service, Professions, Client
from .serializers import EmployeeSerializer, ServiceSerializer, ProfessionsSerializer, ClientSerializer


class EmployeeAPIView(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter,)
    filterset_fields = ['surname', 'profession']
    search_fields = ['surname']
    ordering_fields = ['surname']


class ServiceAPIView(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter,)
    filterset_fields = ['service', 'price']
    search_fields = ['service']
    ordering_fields = ['service', 'price']


class ProfessionsAPIView(viewsets.ModelViewSet):
    queryset = Professions.objects.all()
    serializer_class = ProfessionsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter,)
    filterset_fields = ['profession']
    search_fields = ['profession']
    ordering_fields = ['profession']


class ClientAPIView(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter,)
    filterset_fields = ['name', 'telephone']
    search_fields = ['telephone']
    ordering_fields = ['name']
