from django.contrib import admin
from .models import Poll, Choice, Newspaper, Partisanlean


admin.site.register(Choice)
admin.site.register(Poll)
admin.site.register(Newspaper)
admin.site.register(Partisanlean)

