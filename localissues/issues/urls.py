from django.urls import path, include, re_path
from . import views

# app_name = 'issues'
urlpatterns = [
    path('', views.index, name='index'),
    re_path('/create-issue/', views.create_issue, name='create'),
    re_path('/thanks/', views.thanks, name='thanks'),
    re_path('issues/', views.show_all, name='issues'),
    re_path('issue/(?P<issue_pk>[0-9]+)/$', views.show_issue, name='issue'),
    re_path('delete-issue/(?P<issue_pk>[0-9]+)/$', views.delete_issue, name='delete-issue'),
]