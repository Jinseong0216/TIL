import requests
from pprint import pprint


def get_author_other_books(title):
    URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'
    params = { 'TTBKey': 'ttbpnum23781219001', 
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
        position = response['item'][0]['author'].index(' (지은이)')
        searched_author = response['item'][0]['author'][:position]

        params = { 'TTBKey': 'ttbpnum23781219001', 
                'Query': searched_author,
                'QueryType': 'Author', 
                'MaxResults': 100, 
                'start': 1,
                'SearchTarget': 'Book',
                'output': 'js',
                'Version': '20131101',}
        response = requests.get(URL, params=params).json()
    
        result =[]
        L = len(response['item'])
        if (L == 1): 
            return None
        else:
            i = 0
            while (len(result) < 5) and (i < L-1):
                if response['item'][i]['title'] != title:
                    result.append(response['item'][i]['title'])
                i += 1
            return {f'"{title}"의 저자 "{searched_author}"의 다른 도서 목록' : result}

# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(get_author_other_books('베니스의 상인'), width=120)
    pprint(get_author_other_books('죄와 벌'), width=120)
    pprint(get_author_other_books('*'), width=120)
