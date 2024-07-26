import requests
from pprint import pprint


def get_bestseller_books():
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
    
    indices = []
    for i in range(len(response['item'])):
        indices.append((response['item'][i]['salesPoint'], i))
    
    indices.sort(reverse = True)

    result = []
    for point_i in indices:
        title_point = {'제목': response['item'][point_i[1]]['title'], '판매지수':response['item'][point_i[1]]['salesPoint']}
        result.append(title_point)
    
    return result


# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(get_bestseller_books())
