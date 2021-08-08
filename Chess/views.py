from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from . import urls

import json
import time
import os


def index(request):
	return render(request, "index.html")


def twoPlayerGame(request):
	return render(request, "two_player_game.html")


def handler404(request, *_):
	return render(request, "404.html")


def handler500(request, *_):
	return render(request, "500.html")
