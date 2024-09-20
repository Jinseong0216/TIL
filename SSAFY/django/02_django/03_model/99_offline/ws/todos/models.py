from django.db import models

# Create your models here.
# 할 일 목록을 위한 모델을 정의

# class Todo(models.Model):
#     # 할 일을 저장
#     work = models.CharField(max_length=10)
#     # 완료 여부를 저장
#     # 언제 만들었는지를 저장
#     is_completed = models.BooleanField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)