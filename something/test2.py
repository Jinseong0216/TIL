import requests
from pprint import pprint
import math


def get_users_books(title):
    URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'
    params = { 'ttbkey': 'ttbpnum23781219001', 
              'Query': title,
              'QueryType': 'Title', 
              'MaxResults': 1, 
              'start': 1,
              'SearchTarget': 'Book',
              'output': 'js',
              'Version': '20131101',}
    response = requests.get(URL, params=params).json()
    if response['item'] == []: return None
    else:
        isbn13 = response['item'][0]['isbn13']
        URL = 'http://www.aladin.co.kr/ttb/api/ItemLookUp.aspx'
        params = { 'TTBKey': 'ttbpnum23781219001', 
              'ItemId': isbn13,
              'output': 'js',
              'Version': '20131101',
              'OptResult': 'usedList'}

        response = requests.get(URL, params=params).json()
        return response

# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(get_users_books('죄와 벌'))
#    pprint(get_users_books('로미오와 줄리엣'))
#    pprint(get_users_books('*'))
