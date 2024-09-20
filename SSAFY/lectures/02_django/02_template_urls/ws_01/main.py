import requests

API_URL = 'https://www.aladin.co.kr/ttb/api/ItemList.aspx'
API_KEY = 'keyimport requests'

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
        '국제 표준 도서 번호': item['isbn'],
        '제목': item['title'],
        '출간일': item['pubDate'],
        '저자': item['author'],
    }
    result.append(info)

print(result)