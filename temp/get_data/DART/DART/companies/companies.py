import sys
import csv
import dart_fss as dart

# DART API 키 설정
api_key = 'c4a4aae37470052f3cde859c23811db20ef18539'
dart.set_api_key(api_key)

# sys.stdout 인코딩을 utf-8로 변경 (Windows에서 CP949 오류 해결)
sys.stdout.reconfigure(encoding='utf-8-sig')

# 기업 리스트 가져오기
crp_list = dart.get_corp_list()

# CSV 파일 저장
output_file = 'corporate_info.csv'

# 헤더 정의
header = [
    '기업 번호 (corp_code)',
    '기업 이름 (corp_name)',    
    '주식 번호 (stock_code)',
    '수정 일자 (modify_date)',
    '섹터 (sector)',
    '상품 (product)',
    '법인 구분 (corp_cls)',
]

with open(output_file, 'w', newline='', encoding='utf-8-sig') as csvfile:
    writer = csv.writer(csvfile)
    # 헤더 작성
    writer.writerow(header)
    
    for corp in crp_list:
        data = corp.info
        # 데이터 추출
        corp_code = data.get("corp_code")
        corp_name = data.get("corp_name")
        stock_code = data.get("stock_code", None)
        modify_date = data.get("modify_date", None)
        sector = data.get("sector", None)
        product = data.get("product", None)
        corp_cls = data.get("corp_cls", None)  # 법인 구분: Y, K, N, E
        
        # 데이터 쓰기
        writer.writerow([
            corp_code,
            corp_name,
            stock_code,
            modify_date,
            sector,
            product,
            corp_cls
        ])

print(f"기업 정보를 {output_file}에 저장했습니다.")
