from django.http import HttpResponse
from django import http
from django.urls import path
from django.shortcuts import render

def home(request):
    context = {
        'E': 3,
    }
    return render(request, 'home.html', context)

def pupil(request):
    context = {
        'E': 3,
    }
    return render(request, 'pupil.html', context)