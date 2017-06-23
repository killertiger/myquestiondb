from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView

from questiondb import views

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='question')),
    url(r'^question/$', views.QuestionListView.as_view(), name='question-list'),
    url(r'^question/create/$', views.QuestionCreateView.as_view(), name='question-create'),
    url(r'^question/create/(?P<question_type>[a-zA-Z])$', views.QuestionCreateView.as_view(), name='question-create'),
    url(r'^question/(?P<pk>[0-9]+)/$', views.QuestionUpdateView.as_view(), name='question-update'),
    url(r'^question/(?P<pk>\d+)/delete$', views.QuestionDeteleView.as_view(), name='question-delete'),
]
