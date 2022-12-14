from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def monthly_challenge(request, month):
    challenge_text = None
    if month == 'january':
        challenge_text = "january goal!"
    elif month == 'february':
        challenge_text = "february goal!"
    elif month == 'march':
        challenge_text = "march goal!"
    else:
        return HttpResponseNotFound("This month isn't supported yet.")
    return HttpResponse(challenge_text)
