from django.urls import path

from . import views

import json

urlpatterns = [
	path("", views.index, name="index"),
	path("twoplayers", views.twoPlayerGame, name="twoplayers"),
]
