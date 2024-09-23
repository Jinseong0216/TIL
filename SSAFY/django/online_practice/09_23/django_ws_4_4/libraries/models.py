from django.db import models

# Create your models here.
class Book(models.Model):
    Isbn = models.CharField(max_length=13)
    Author = models.TextField()
    Title = models.TextField()
    Category_name = models.TextField(db_column='Category name')
    Category_id = models.IntegerField(db_column='Category id')
    price = models.IntegerField()
    Fixed_price = models.BooleanField(db_column='Fixed price')
    Pub_date = models.DateField(db_column='Pub date')