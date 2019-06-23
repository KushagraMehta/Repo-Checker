from django.conf.urls import include
from django.urls import path
from user import views

urlpatterns = [
    path('', views.home_page.as_view(), name='index'),
    path('user/<str:username>', views.repo_explorer.as_view(), name='graph'),
]
