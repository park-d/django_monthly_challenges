from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def january(request):
    return HttpResponse("january goal!")


def february(request):
    return HttpResponse("february goal!")


def march(request):
    return HttpResponse("march goal!")


def april(request):
    return HttpResponse("april goal!")


def may(request):
    return HttpResponse("may goal!")


def june(request):
    return HttpResponse("june goal!")


def july(request):
    return HttpResponse("july goal!")


def august(request):
    return HttpResponse("august goal!")


def september(request):
    return HttpResponse("september goal!")


def october(request):
    return HttpResponse("october goal!")


def november(request):
    return HttpResponse("november goal!")


def december(request):
    return HttpResponse("december goal!")
