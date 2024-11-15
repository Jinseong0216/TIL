import requests
import pandas as pd
import os  # 파일 존재 여부 확인용

# JSON 데이터를 가져와 CSV 파일로 변환하는 함수
def fetch_and_convert_to_csv(topFinGrpNo, pageNo, products_csv_filename, options_csv_filename):
    api_key = 'adacd855f3d03e39ba22a2a45a5f8158'
    is_continue = True
    while is_continue:
        url = f"http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={api_key}&topFinGrpNo={topFinGrpNo}&pageNo={pageNo}"
        # 데이터 가져오기
        response = requests.get(url)
        data = response.json()
        result = data.get('result', {})
        is_continue = bool(result.get('max_page_no', {}) != result.get('now_page_no', {}))

        # 상품 목록 및 옵션 목록 추출
        products = result.get('baseList', [])
        options = result.get('optionList', [])

        # 상품 목록을 DataFrame으로 변환
        product_records = [{
            'topFinGrpNo': str(topFinGrpNo),  # 문자열로 변환
            'dcls_month': product.get('dcls_month', ''),
            'fin_co_no': product.get('fin_co_no', ''),
            'fin_prdt_cd': product.get('fin_prdt_cd', ''),
            'kor_co_nm': product.get('kor_co_nm', ''),
            'fin_prdt_nm': product.get('fin_prdt_nm', ''),
            'join_way': product.get('join_way', ''),
            'mtrt_int': product.get('mtrt_int', ''),
            'spcl_cnd': product.get('spcl_cnd', ''),
            'join_deny': product.get('join_deny', ''),
            'join_member': product.get('join_member', ''),
            'etc_note': product.get('etc_note', ''),
            'max_limit': product.get('max_limit', ''),
            'dcls_strt_day': product.get('dcls_strt_day', ''),
            'dcls_end_day': product.get('dcls_end_day', ''),
            'fin_co_subm_day': product.get('fin_co_subm_day', '')
        } for product in products]
        
        # 옵션 목록을 DataFrame으로 변환
        option_records = [{
            'topFinGrpNo': str(topFinGrpNo),  # 문자열로 변환
            'dcls_month': option.get('dcls_month', ''),
            'fin_co_no': option.get('fin_co_no', ''),
            'fin_prdt_cd': option.get('fin_prdt_cd', ''),
            'intr_rate_type': option.get('intr_rate_type', ''),
            'intr_rate_type_nm': option.get('intr_rate_type_nm', ''),
            'rsrv_type': option.get('rsrv_type', ''),
            'rsrv_type_nm': option.get('rsrv_type_nm', ''),
            'save_trm': option.get('save_trm', ''),
            'intr_rate': option.get('intr_rate', ''),
            'intr_rate2': option.get('intr_rate2', '')
        } for option in options]
        
        # DataFrame 생성
        products_df = pd.DataFrame(product_records)
        options_df = pd.DataFrame(option_records)

        # DataFrame이 비어있지 않으면 CSV로 저장
        if not products_df.empty:
            products_df.to_csv(products_csv_filename, index=False, mode='a', header=not os.path.exists(products_csv_filename), encoding='utf-8-sig')
            print(f"{products_csv_filename}에 {topFinGrpNo}의 {pageNo}페이지에서 products 데이터가 저장되었습니다.")
        if not options_df.empty:
            options_df.to_csv(options_csv_filename, index=False, mode='a', header=not os.path.exists(options_csv_filename), encoding='utf-8-sig')
            print(f"{options_csv_filename}에 {topFinGrpNo}의 {pageNo}페이지에서 options 데이터가 저장되었습니다.")

        pageNo += 1
    return

# 데이터를 가져와 각각의 CSV로 변환 및 저장
topFinGrpNo_list = ["020000", "030200", "030300", "050000", "060000"]
for topFinGrpNo in topFinGrpNo_list:
    fetch_and_convert_to_csv(topFinGrpNo, 1, "products.csv", "options.csv")
