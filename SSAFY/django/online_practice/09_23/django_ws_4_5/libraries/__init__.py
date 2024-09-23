import requests
import pprint

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
    print((response['item'][0]['categoryId']))



if __name__ == '__main__':
    result = get_new_special_books()
    pprint.pprint(result)


