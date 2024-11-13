import dart_fss as dart
import pandas as pd
import requests
import xml.etree.ElementTree as ET
import zipfile
import io
from bs4 import BeautifulSoup

# api_key 설정
api_key = 'c4a4aae37470052f3cde859c23811db20ef18539'
dart.set_api_key(api_key=api_key)

# 기업번호 설정 (예시: 삼성전자)
corp_code = '00126380'  # 삼성전자의 기업번호
url_json = "https://opendart.fss.or.kr/api/list.json"

params = {
    'crtfc_key': api_key,
    'corp_code': corp_code,
    'pblntf_ty': 'A',  # 사업보고서
    'bgn_de': '20230101'  # 사업보고서 시작일
}

response = requests.get(url_json, params=params)
res = response.json()

# 데이터가 없는 경우 처리
if res['status'] == '013':
    print(f'{corp_code}, 사업보고서 개수: 0')

# 사업보고서 목록 출력
df_imsi = pd.DataFrame(res['list'])
print('==================== 보고서 목록 ====================')
print(df_imsi)

# 사업보고서 문서 가져오기 (rcept_no는 실제 보고서의 접수번호)
url = 'https://opendart.fss.or.kr/api/document.xml'
params = {
    'crtfc_key': api_key,
    'rcept_no': '20230307000542',  # 예시로 사용되는 접수번호
}

r = requests.get(url, params=params)

# XML 파싱
try:
    tree = ET.XML(r.text)
    status = tree.find('status').text
    message = tree.find('message').text
    if status != '000' and status != '014':
        raise ValueError({'status': status, 'message': message})
except ET.ParseError as e:
    print(f"XML 파싱 오류: {e}")

# XML 데이터 압축 해제 후 내용 추출
zf = zipfile.ZipFile(io.BytesIO(r.content))
info_list = zf.infolist()
fnames = sorted([info.filename for info in info_list])

# XML 텍스트를 리스트에 저장
xml_text_list = []
for fname in fnames:
    xml_data = zf.read(fname)
    try:
        xml_text = xml_data.decode('euc-kr')
    except UnicodeDecodeError:
        xml_text = xml_data.decode('utf-8')
    xml_text_list.append(xml_text)

print('==================== 파일 내용 확인 ====================')
print(fnames)
print(xml_text_list[0])  # XML 파일의 첫 번째 내용 출력

# 필요한 섹션을 추출 (회사 개요, 사업 내용 등)
# 예시로 "회사 개요", "사업의 내용", "연결대상 종속회사 현황" 등 추출하기

from lxml import etree

# XML 파일을 lxml로 파싱 (오류가 있을 경우)
def extract_section_titles_and_page_numbers(file_path):
    # lxml의 recover=True 옵션을 사용하여 XML 형식 오류 처리
    parser = etree.XMLParser(recover=True)
    tree = etree.parse(file_path, parser)
    root = tree.getroot()
    
    sections = []
    
    # BODY 태그 내에서 목차 항목을 찾기
    for table in root.iter('TABLE'):
        # 각 행에서 목차 제목과 페이지 번호 추출
        rows = table.findall('TBODY/TR')
        for row in rows:
            cells = row.findall('TD')
            if len(cells) > 2:
                # 1번째 칸: 항목 제목, 4번째 칸: 페이지 번호
                title = cells[0].text.strip() if cells[0].text else ''
                page = cells[3].text.strip() if cells[3].text else ''
                if title and page:
                    sections.append((title, page))
    
    return sections

# XML 파일 경로 지정
file_path = '20230307000542.xml'  # 실제 파일 경로로 변경

# 목차 추출
sections = extract_section_titles_and_page_numbers(file_path)

# 추출된 목차 출력
if sections:
    print("=== 사업보고서 목차 ===")
    for title, page in sections:
        print(f"목차 제목: {title}, 페이지 번호: {page}")
else:
    print("목차를 찾을 수 없습니다.")

