from django.shortcuts import render

from .models import *


def clinic(request):
    services = Service.objects.values('pk', 'service', 'description').order_by('pk')
    context = {'services': services}
    return render(request, 'home.html', context)


def services(request):
    all_services = Service.objects.values('pk', 'service', 'description')
    context = {'all_services': all_services}
    return render(request, 'services.html', context)


def detailed_services(request, pk):
    service = Service.objects.get(pk=pk)
    context = {'service': service}
    return render(request, 'detailed_services.html', context)


def prices(request):
    services = Service.objects.all().order_by("id")
    context = {'services': services}
    return render(request, 'prices.html', context)


def our_specialists(request):
    specialists = Employee.objects.all()
    context = {'specialists': specialists}
    return render(request, 'our_specialists.html', context)


def detailed_by_specialist(request, pk):
    specialist = Employee.objects.get(pk=pk)
    context = {'specialist': specialist}
    return render(request, 'detailed_by_specialist.html', context)


def all_contacts(request):
    contacts = Contacts.objects.all().order_by("id")
    information = Information.objects.values("working_hours")[0]
    all_info = information['working_hours'].partition('(')
    working_hours = all_info[0]
    lunch_break = all_info[2].rstrip(')')
    context = {'contacts': contacts,
               'information': information,
               'working_hours': working_hours,
               'lunch_break': lunch_break}
    return render(request, 'contacts.html', context)
