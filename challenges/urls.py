from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="challenges-list"), #/challenges/
    path("<int:month>", views.monthly_challenge_num),
    path("<str:month>", views.monthly_challenge_str, name = "month-challenge")
]
