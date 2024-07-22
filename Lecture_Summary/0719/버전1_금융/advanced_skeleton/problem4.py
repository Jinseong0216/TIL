import pprint
import requests

# 상품과 옵션 정보들을 담고 있는 새로운 객체를 만들어 반환하시오.
# [힌트] 상품 리스트와 옵션 리스트를 금융상품 코드를 기준으로 매칭할 수 있습니다.
# [힌트] 아래와 같은 순서로 데이터를 출력하며 진행합니다.
# 1. 응답을 json 형식으로 변환합니다.
# 2. key 값이 "result" 인 데이터를 변수에 저장합니다.
# 3. 2번의 결과 중 key 값이 "baseList" 인 데이터를 변수에 저장합니다.
# 4. 2번의 결과 중 key 값이 "optionList" 인 데이터를 변수에 저장합니다.
# 5. 3번에서 저장된 변수를 순회하며, 4번에서 저장된 값들에서 금융 상품 코드가 
#     같은 모든 데이터들을 가져와 새로운 딕셔너리로 저장합니다.
#     저장 시, 명세서에 맞게 출력되도록 저장합니다.
# 6. 5번에서 만든 딕셔너리를 결과 리스트에 추가합니다.


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
    option_list = response['result']['optionList']
    base_list = response['result']['baseList']

    new_list = []
    for option in response['result']['optionList']:
        new_dict = {}
        new_dict['금융상품코드'] = option['fin_prdt_cd']
        new_dict['저축 금리'] = option['intr_rate'] #보류
        new_dict['저축 기간'] = option['save_trm']
        new_dict['저축금리유형'] = option['intr_rate_type']
        new_dict['저축금리유형명'] = option['intr_rate_type_nm']
        new_dict['최고 우대금리'] = option['intr_rate2']
        new_list.append(new_dict)
    
    new_list2 = {}
    for option in new_list:
        if option['금융상품코드'] not in new_list2: 
            new_list2[option['금융상품코드']] = { 
                '금리정보' : [
                    {'저축 금리': option['저축 금리'], '저축 기간': option['저축 기간'],'저축금리유형': option['저축금리유형'],'저축금리유형명': option['저축금리유형명'],'최고 우대금리': option['최고 우대금리']}
                    ]
                    }
        else: 
            new_list2[option['금융상품코드']]['금리정보'].append({ '금리정보' : 
                                           [{'저축 금리':option['저축 금리'],
                             '저축 기간': option['저축 기간'],
                             '저축금리유형': option['저축금리유형'],
                             '저축금리유형명': option['저축금리유형명'],
                             '최고 우대금리': option['최고 우대금리']}]})

    fin_cd_list = {}
    for base in base_list:
        fin_cd_list[base['fin_prdt_cd']] = [base['kor_co_nm'], base['fin_prdt_nm'] ] 

    new_list3 = []
    for key,value in new_list2.items():
        new_dict = {}
        dict1 = {'금융 상품명': fin_cd_list[key][1]}
        dict2 = {'금융 회사명': fin_cd_list[key][0]}
        new_dict.update(new_list2[key])
        new_dict.update(dict1)
        new_dict.update(dict2)
        new_list3 += [new_dict]

    return new_list3
  

if __name__ == '__main__':
    # json 형태의 데이터 반환
    result = get_deposit_products()
    # prrint.prrint(): json 을 보기 좋은 형식으로 출력
    pprint.pprint(result)


