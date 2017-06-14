from django.conf.urls import url, include
from django.contrib import admin

from questiondb import views

urlpatterns = [
    url(r'^question/$', views.QuestionListView.as_view(), name='question-list'),
    url(r'^question/create/$', views.QuestionCreateView.as_view(), name='question-create'),
]
