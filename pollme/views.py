from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = f'<h1>The current time is {now}</h1>'
    return HttpResponse(html)