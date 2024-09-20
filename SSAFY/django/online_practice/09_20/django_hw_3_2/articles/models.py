from django.db import models

# Create your models here.

class Article(models.Model):
    # id는 안만들어도 자동으로 만들어 주는듯
    # id = models.IntegerField()
    title = models.CharField(max_length=15)
    content = models.TextField()