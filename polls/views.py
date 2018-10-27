from django.shortcuts import render
from django.http import HttpResponse
import datetime


def polls_list(request):
	now = datetime.datetime.now()
	context = { "GOT" : now }
	return render(request, 'polls/pollslist.html', context)

# Create your views here.
