from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Домашка по 4 занятию")

def empty(request):
    return HttpResponse("Тут пусто")
# Create your views here.
