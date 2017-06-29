from django.db import transaction
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import DeleteView
from django.views.generic import UpdateView
from extra_views import SearchableListMixin
from django.db import models
from rest_framework import generics
from rest_framework import viewsets

from questiondb.forms import AlternativeFormSetCreate, AlternativeFormSetUpdate
from questiondb.models import Question, Category, CategorySerializer


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

def get_categories_recursive(categories):
    response_data = []
    for category in categories:
        categoryObj = {'id': category.pk, 'text': category.name}
        categoryObj['children'] = get_categories_recursive(category.children)
        response_data.append(categoryObj)

    return response_data

def get_categories(request):
    categories = Category.objects.filter(parent__isnull=True)
    response_data = get_categories_recursive(categories)

    return JsonResponse(response_data, safe=False)

def create_category(request):
    category = Category(name=request.POST["name"], parent_id=request.POST["parent_id"])
    category.Save()

    return HttpResponse(category.pk)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryAPICreate(generics.ListCreateAPIView):
    queryset = Category.objects.filter(parent__isnull=True)
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        serializer.save()


class CategoryAPIDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
