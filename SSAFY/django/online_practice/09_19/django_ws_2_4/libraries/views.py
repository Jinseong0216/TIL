import requests
from django.shortcuts import render

API_URL = 'https://www.aladin.co.kr/ttb/api/ItemList.aspx'
API_KEY = 'ttbpnum23781219001'

# Create your views here.
def index(request):
    return render(request, 'index.html')

def recommend(request):
    params = {
        'ttbkey': API_KEY,
        'QueryType': 'ItemNewSpecial',
        'MaxResults': '50',
        'start': '1',
        'SearchTarget': 'Book',
        'output': 'js',
        'Version': '20131101'
    }

    response = requests.get(API_URL, params=params).json()

    result = []
    for item in response['item']:
        info = {
            'isbn': item['isbn'],
            'title': item['title'],
            'pubDate': item['pubDate'],
            'author': item['author'],
        }
        result.append(info)
    context = {
        'result': result
    }
    return render(request, 'recommend.html', context)


def bestseller(request):
    params = {
        'ttbkey': API_KEY,
        'QueryType': 'Bestseller',
        'MaxResults': '50',
        'start': '1',
        'SearchTarget': 'Book',
        'output': 'js',
        'Version': '20131101'
    }

    response = requests.get(API_URL, params=params).json()

    result = []
    for item in response['item']:
        info = [int(item.get('salesPoint')),
                {
            'isbn': item.get('isbn'),
            'title': item.get('title'),
            'pubDate': item.get('pubDate'),
            'author': item.get('author'),
            'bestDuration': item.get('bestDuration'),
        }]
        result.append(info)
        result.sort(reverse=True)
    context = {
        'result': [book_info[1] for book_info in result], 
    }
    return render(request, 'bestseller.html', context)