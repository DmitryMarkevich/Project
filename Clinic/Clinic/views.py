from django.http import HttpResponse
from django.shortcuts import render


def about(reguest):
    return HttpResponse('<h1>Это страница сайта Clinic</h1>')



