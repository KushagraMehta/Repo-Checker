from django.conf.urls import include
from django.urls import path
from user import views

urlpatterns = [
    path('', views.home_page.as_view(), name='index'),
]
