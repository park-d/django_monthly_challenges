from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def monthly_challenge_num(request, month):
    challenge_text = None
    if month == 1:
        challenge_text = "january goal!"
    elif month == 2:
        challenge_text = "february goal!"
    elif month == 3:
        challenge_text = "march goal!"
    else:
        return HttpResponseNotFound("This month isn't supported yet.")
    return HttpResponse(challenge_text)

def monthly_challenge_str(request, month):
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
