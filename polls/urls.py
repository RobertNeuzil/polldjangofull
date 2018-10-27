
from django.urls import path, include
from . import views

urlpatterns = [
	path('list/', views.polls_list)
]
