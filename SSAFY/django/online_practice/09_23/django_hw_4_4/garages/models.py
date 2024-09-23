from django.db import models

# Create your models here.
class Garage(models.Model):
    location = models.CharField(max_length=200)
    capacity = models.IntegerField()
    is_parking_avaliable = models.BooleanField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()

# garage = Garage(location='서울', capacity=30, is_parking_avaliable=0, opening_time='08:00:00', closing_time='22:00:00')
# garage = Garage(location='부산', capacity=20, is_parking_avaliable=1, opening_time='07:00:00', closing_time='23:00:00')
# garage = Garage(location='독도', capacity=40, is_parking_avaliable=1, opening_time='09:00:00', closing_time='20:00:00')