from django.shortcuts import render
from django.http import HttpResponse
from .models import Poll 


def polls_list(request):
	'''

	renderts pollslist.html template which lists
	all currently available polls

	'''
	polls = Poll.objects.all()
	context = { 'polls': polls }
	return render(request, 'polls/pollslist.html', context)

# Create your views here.
