from django.http import HttpResponse
from django.shortcuts import render

import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = f'<h1>The current time is {now}</h1>'
    return HttpResponse(html)

def home(request):
	return render(request, 'home.html')