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
    # if response['item'] == []: return None
    # else:
    #     isbn13 = response['item'][0]['isbn13']
    #     URL = 'http://www.aladin.co.kr/ttb/api/ItemLookUp.aspx'
    #     params = { 'TTBKey': 'ttbpnum23781219001', 
    #           'ItemId': isbn13,
    #           'output': 'js',
    #           'Version': '20131101',
    #           'OptResult': 'usedList'}

        # response = requests.get(URL, params=params).json()
        # aladinUsed = response['item'][0]['subInfo']['usedList']['aladinUsed']
        # spaceUsed = response['item'][0]['subInfo']['usedList']['spaceUsed']
        # userUsed = response['item'][0]['subInfo']['usedList']['userUsed']
        
        # comparing_list = [aladinUsed, spaceUsed, userUsed]
        # min_Price = float('inf')
        # j = 0
        # for i in range(1,3):
        #     if comparing_list[i]['minPrice'] < min_Price:
        #          min_Price = comparing_list[i]['minPrice']
        #          j = i
        # if min_Price == 0:
        #     return '수정해야함'
        # else:
        #     if i == 0:
        #         return f'도서 "{title}"의 가장 저렴한 중고는 알라딘이 보유 중이며, {min_Price}에 판매 중입니다.'
        #     elif i == 1:
        #         return f'도서 "{title}"의 가장 저렴한 중고는 광활한 우주점이 보유 중이며, {min_Price}에 판매 중입니다.'
        #     else:
        #         return f'도서 "{title}"의 가장 저렴한 중고는 개인 회원이 보유 중이며, {min_Price}에 판매 중입니다.'
    return response
# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
#    pprint(get_users_books('죄와 벌'))
    pprint(get_users_books('로미오와 줄리엣'))
#    pprint(get_users_books('*'))
