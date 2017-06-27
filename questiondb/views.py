from django.db import transaction
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import DeleteView
from django.views.generic import UpdateView
from extra_views import SearchableListMixin

from questiondb.forms import AlternativeFormSetCreate, AlternativeFormSetUpdate
from questiondb.models import Question


class QuestionListView(generic.ListView):
    model = Question


class QuestionCreateView(generic.CreateView):
    model = Question
    fields = ["title", "degree_of_dificulty", "category", "body_html"]
    success_url = reverse_lazy('question-list')

    def get_context_data(self, **kwargs):
        data = super(QuestionCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['alternatives'] = AlternativeFormSetCreate(self.request.POST)
        else:
            data['alternatives'] = AlternativeFormSetCreate()

        if 'question_type' in self.kwargs:
            data['question_type'] = self.kwargs['question_type']

        return data

    def form_valid(self, form):
        context = self.get_context_data()
        alternatives = context['alternatives']
        form.instance.question_type = context['question_type']

        if context['question_type'] == 't':
            form.save()
        else:
            with transaction.atomic():
                self.object = form.save()

                if alternatives.is_valid():
                    alternatives.instance = self.object
                    alternatives.save()

        return super(QuestionCreateView, self).form_valid(form)


class QuestionUpdateView(UpdateView):
    model = Question
    fields = ["title", "degree_of_dificulty", "category", "body_html"]
    success_url = reverse_lazy('question-list')

    def get_context_data(self, **kwargs):
        data = super(QuestionUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['alternatives'] = AlternativeFormSetUpdate(self.request.POST, instance=self.object)
        else:
            data['alternatives'] = AlternativeFormSetUpdate(instance=self.object)

        data['question_type'] = self.object.question_type

        return data

    def form_valid(self, form):
        context = self.get_context_data()
        alternatives = context['alternatives']

        if context['question_type'] == 't':
            form.save()
        else:
            with transaction.atomic():
                self.object = form.save()

                if alternatives.is_valid():
                    alternatives.instance = self.object
                    alternatives.save()

        return super(QuestionUpdateView, self).form_valid(form)


class QuestionDeteleView(DeleteView):
    model = Question
    success_url = reverse_lazy('question-list')
