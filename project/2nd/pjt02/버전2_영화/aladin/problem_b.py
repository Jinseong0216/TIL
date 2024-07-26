import requests
from pprint import pprint


def get_best_review_books():
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
    
    result = []
    for info in response['item']:
        if info['customerReviewRank'] >= 9:
            result.append(info)

    return result

# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(get_best_review_books())
