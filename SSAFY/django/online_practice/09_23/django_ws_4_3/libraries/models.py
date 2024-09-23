from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.TextField()
    pubdate = models.DateField()
    price = models.IntegerField()
    adult = models.BooleanField()

    
    
    # book = Book(title='홍길동전', author='허균', pubdate='1994-07-25', price=3000, adult=False)
    # book = Book(title='난중일기', author='이순신', pubdate='2015-01-21', price=0, adult=True)
    # book = Book(title='세종실록', author='이도', pubdate='1397-05-15', price=0, adult=False)
