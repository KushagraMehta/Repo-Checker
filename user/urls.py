from django.conf.urls import include
from django.urls import path
from user import views

urlpatterns = [
    path('', views.home_page.as_view(), name='index'),
    path('user/<str:username>', views.repo_explorer.as_view(), name='graph'),
    path('api/<str:username>', views.user_data.as_view(), name="user"),
    path('test', views.test, name="test"),
]
