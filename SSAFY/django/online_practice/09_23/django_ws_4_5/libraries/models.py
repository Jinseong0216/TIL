from django.db import models
import requests

# Create your models here.
class Book(models.Model):
    isbn = models.CharField(max_length=10)
    author = models.TextField()
    title = models.TextField()
    category_name = models.TextField()
    category_id = models.IntegerField()
    price = models.IntegerField()
    fixed_price = models.BooleanField()
    pub_date = models.DateField()


    @classmethod
    def insert_data(cls):
        
        def get_new_special_books():
            API_URL = 'http://www.aladin.co.kr/ttb/api/ItemList.aspx'
            params = { 'ttbkey': 'ttbpnum23781219001', 
                    'QueryType': 'ItemNewSpecial', 
                    'MaxResults': 10, 
                    'start': 1,
                    'SearchTarget': 'Book',
                    'output': 'JS',
                    'Version': '20131101',}
            response = requests.get(API_URL, params=params).json()
            return response['item']
        
        data = get_new_special_books()
        
        for item in data:
            book = cls(isbn=item['isbn'], author=item['author'], title=item['title'], category_name=item['categoryName'],
                       category_id=item['categoryId'], price=item['priceSales'], fixed_price=item['fixedPrice'], pub_date=item['pubDate'])
            book.save()

# django shell에서 아래 코드 실행
# Book.insert_data()