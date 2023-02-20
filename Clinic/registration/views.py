from django.shortcuts import render
from datetime import datetime
from Clinic_info.models import Client
from registration.forms import RegistrationForm


def new_registration(request):
    form = RegistrationForm()
    registration = 0
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            client = Client(
                name=form.cleaned_data["name"],
                telephone=form.cleaned_data["telephone"],
                email=form.cleaned_data["email"],
                service=form.cleaned_data["service"],
            )
            client.save()
            registration = 1

    context = {'form': form, 'registration': registration}
    return render(request, 'registration.html', context)


def get_registrants(request):
    if request.user.is_authenticated:
        all_client = Client.objects.all().order_by('-created_on')
        count_client = Client.objects.count()
        context = {'all_client': all_client, 'count_client': count_client}
        return render(request, 'all_client.html', context)

    else:
        return render(request, 'no_access.html')


def get_registrants_detail(request):
    current_datetime = datetime.now()
    if request.path_info == '/registrants_detail_day/':
        all_client = Client.objects.filter(created_on__day=current_datetime.day).order_by('-created_on')
    else:
        all_client = Client.objects.filter(created_on__month=current_datetime.month).order_by('-created_on')

    context = {'all_client': all_client}
    return render(request, 'all_client.html', context)

