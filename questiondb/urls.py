from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from questiondb import views


#router =  routers.DefaultRouter()
#router.register(r'categories', views.CategoryViewSet)

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='question')),
    url(r'^question/$', views.QuestionListView.as_view(), name='question-list'),
    url(r'^question/create/$', views.QuestionCreateView.as_view(), name='question-create'),
    url(r'^question/create/(?P<question_type>[a-zA-Z])/$', views.QuestionCreateView.as_view(), name='question-create'),
    url(r'^question/(?P<pk>[0-9]+)/$', views.QuestionUpdateView.as_view(), name='question-update'),
    url(r'^question/(?P<pk>\d+)/delete/$', views.QuestionDeteleView.as_view(), name='question-delete'),
#    url(r'^category/$', views.get_categories, name='categories'),
#    url(r'^category/create/$', views.create_category, name='category-create'),
    url(r'^api/categories/$', views.CategoryAPICreate.as_view(), name='api-category-create'),
    url(r'^api/categories/(?P<pk>[0-9]+)/$', views.CategoryAPIDetails.as_view(), name='api-category-detail'),
#    url(r'^api/$', include(router.urls)),
#    url(r'^api/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
