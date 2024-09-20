import requests
import pprint

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
    books_list = [
                  {'국제 표준 도서 번호': response['item'][i]['isbn13'], 
                   '저자': response['item'][i]['author'], 
                   '제목': response['item'][i]['title'], 
                   '출간일': response['item'][i]['pubDate']} 
                  for i in range(len(response['item']))
                  ]
    return books_list


if __name__ == '__main__':
    result = get_new_special_books()
    pprint.pprint(result)

