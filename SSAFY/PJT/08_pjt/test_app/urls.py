from django.urls import path
from . import views

urlpatterns = [
    # README.md 보여주기
    path('', views.index),
    # CSV 데이터를 DataFrame으로 변환 후 반환하기 위함
    path('my_data/', views.my_data),
    # CSV 데이터의 결측치 전처리
    path('my_data_has_null/', views.my_data_has_null),
    # 평균나이 계산
    path('mean_age/', views.mean_age),
    # 내장 메서드 sort()
    path('normal_sort/', views.normal_sort),
    # 우선순위큐
    path('priority_queue/', views.priority_queue),
    # 버블정렬
    path('bubble_sort/', views.bubble_sort),
]

