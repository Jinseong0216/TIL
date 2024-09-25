from django.db import models

# Create your models here.
class Travel(models.Model):
    location = models.CharField(max_length=10)
    plan = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()