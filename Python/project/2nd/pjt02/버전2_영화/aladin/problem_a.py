import requests
from pprint import pprint


def get_author_books():
    URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'
    params = { 'ttbkey': 'ttbpnum23781219001', 
              'Query': '파울로 코엘료',
              'QueryType': 'Author', 
              'MaxResults': 20, 
              'start': 1,
              'SearchTarget': 'Book',
              'output': 'js',
              'Version': '20131101',}
    response = requests.get(URL, params=params).json()
    books_list = []
    for i in range(len(response['item'])): 
        books_list.append(response['item'][i]['title'])
    return books_list


# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(get_author_books())