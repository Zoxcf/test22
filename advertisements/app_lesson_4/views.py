from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Успех успешный!!!!')

def lesson_4(request):
    return HttpResponse('Домашка по 4 занятию')



