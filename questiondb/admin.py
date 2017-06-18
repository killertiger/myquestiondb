from django.contrib import admin

# Register your models here.

from questiondb.models import Question, Alternative

admin.site.register(Question)
admin.site.register(Alternative)