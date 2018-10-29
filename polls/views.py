from django.shortcuts import render
from django.http import HttpResponse
from .models import Poll, Newspaper 


def polls_list(request):
	'''

	renderts pollslist.html template which lists
	all currently available polls

	'''
	polls = Poll.objects.all()
	newspaper = Newspaper.objects.all()
	context = { 'polls': polls, 'newspaper': newspaper }
	return render(request, 'polls/pollslist.html', context)

# Create your views here.
