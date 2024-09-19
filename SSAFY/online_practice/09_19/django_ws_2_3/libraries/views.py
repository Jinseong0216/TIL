from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    return render(request, 'index.html')

def recommend(request):
    
    
    def get_new_special_books():
        API_URL = 'http://www.aladin.co.kr/ttb/api/ItemList.aspx'
        params = { 'ttbkey': 'ttbpnum23781219001', 
                'QueryType': 'ItemNewSpecial', 
                'MaxResults': 50, 
                'start': 1,
                'SearchTarget': 'Book',
                'output': 'JS',
                'Version': '20131101',}
        response = requests.get(API_URL, params=params).json()
        books_list = [  [['제목', response['item'][i]['title']], ['저자', response['item'][i]['author']]]
                        for i in range(len(response['item']))
                        ]   
        return books_list
    

    context = {
        'book_info': get_new_special_books(), 
    }

    return render(request, 'recommend.html', context)


