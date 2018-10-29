
from django.urls import path, include
from . import views


app_name = 'polls'
urlpatterns = [
	path('list/', views.polls_list, name='list')
]
