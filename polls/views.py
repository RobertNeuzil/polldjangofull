from django.shortcuts import render
from django.http import HttpResponse

def polls_list(request):
	return HttpResponse("Polls List")

# Create your views here.
