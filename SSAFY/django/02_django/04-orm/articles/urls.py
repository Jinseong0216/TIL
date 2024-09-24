from django.urls import path
# 명시적 상대경로
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
]
