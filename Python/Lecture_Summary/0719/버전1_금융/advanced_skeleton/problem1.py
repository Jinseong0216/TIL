import pprint
import requests

# 전체 정기예금의 응답을 json 형태로 변환하여 key 값만 출력하시오.
# 공식문서의 요청변수와 예제 요청결과(JSON) 부분을 참고합니다.
# [힌트] 아래와 같은 순서로 데이터를 출력하며 진행합니다.
# 1. 응답을 json 형식으로 변환합니다.
# 2. key 값이 "result" 인 데이터에 모든 정보가 담겨 있습니다.
# 3. key 값이 "result" 인 데이터의 key 값만 출력합니다.

def get_deposit_products():
    # 본인의 API KEY 로 수정합니다.
    api_key = 'a7396cd72039dbb1643a2f3b1ba7dd59'
    url = 'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
    params = {
        'auth': api_key,
        'topFinGrpNo': '020000',
        'pageNo': 1
    }
    # 금융회사 코드 020000(은행), 030200(여신전문), 030300(저축은행), 050000(보험), 050000(보험), 060000(금융투자)
    # 요구사항에 맞도록 이곳의 코드를 수정합니다.

    response = requests.get(url, params = params).json()
    response = response['result'].keys()
    return response
    
    
# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    # json 형태의 데이터 반환
    result = get_deposit_products()
    # prrint.prrint(): json 을 보기 좋은 형식으로 출력
    print(result)
