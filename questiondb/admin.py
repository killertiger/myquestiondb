from django.contrib import admin

# Register your models here.

from questiondb.models import Question, Alternative, Category

admin.site.register(Question)
admin.site.register(Alternative)
admin.site.register(Category)