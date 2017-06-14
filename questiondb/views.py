from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic

from questiondb.models import Question


class QuestionListView(generic.ListView):
    model = Question


class QuestionCreateView(generic.CreateView):
    model = Question
    fields = "__all__"
    success_url = reverse_lazy('question-list')