from django.conf.urls import url
from django.views.generic import RedirectView
from rest_framework.urlpatterns import format_suffix_patterns

from questiondb import views


urlpatterns = [
    url(r'^$', RedirectView.as_view(url='question')),
    url(r'^question/$', views.QuestionListView.as_view(), name='question-list'),
    url(r'^question/create/$', views.QuestionCreateView.as_view(), name='question-create'),
    url(r'^question/create/(?P<question_type>[a-zA-Z])/$', views.QuestionCreateView.as_view(), name='question-create'),
    url(r'^question/(?P<pk>[0-9]+)/$', views.QuestionUpdateView.as_view(), name='question-update'),
    url(r'^question/(?P<pk>\d+)/delete/$', views.QuestionDeteleView.as_view(), name='question-delete'),
    url(r'^api/categories/list_all/$', views.get_categories, name='api-category-list'),
    url(r'^api/categories/$', views.CategoryAPICreate.as_view(), name='api-category-create'),
    url(r'^api/categories/(?P<pk>[0-9]+)/$', views.CategoryAPIDetails.as_view(), name='api-category-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
