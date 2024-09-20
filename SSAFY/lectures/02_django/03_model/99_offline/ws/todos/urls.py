from django.urls import path
from . import views


app_name = 'todos'

urlpatterns = [
    path('index/', views.main, name='main'),
    path('create/', views.create, name='create'),
]