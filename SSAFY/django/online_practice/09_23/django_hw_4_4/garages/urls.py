from django.urls import path
# 명시적 상대경로
from . import views

app_name = 'garages'
urlpatterns = [
    path('', views.index, name='index'),
]