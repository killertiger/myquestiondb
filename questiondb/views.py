from django.shortcuts import render

# Create your views here.
from django.views import generic

from questiondb.models import Question


class QuestionListView(generic.ListView):
    model = Question