import dart_fss as dart
import pandas as pd
import requests
import xml.etree.ElementTree as ET
import zipfile
import io
from bs4 import BeautifulSoup

'''
참조 문서(openDART, 개발가이드):
https://opendart.fss.or.kr/guide/detail.do?apiGrpCd=DS001&apiId=2019003
'''

# api_key setting
api_key = '	c4a4aae37470052f3cde859c23811db20ef18539'
dart.set_api_key(api_key=api_key)

# 상장 기업명
# ====================================================================================================
# ====================================================================================================
corp_list = dart.api.filings.get_corp_code()
corp_df = pd.DataFrame.from_dict(corp_list)
corp_df = corp_df.dropna(subset = 'stock_code').sort_values('modify_date',ascending=False).reset_index(drop=True)
corp_df['done_YN'] = "N"
print('==================== 상장 기업명 ====================')
print(corp_df)


# 보고서 목록
# ====================================================================================================
# ====================================================================================================
corp_code = '00126380' # 삼성전자의 기업번호
url_json = "https://opendart.fss.or.kr/api/list.json"

params = {
    'crtfc_key' : api_key,
    'corp_code' : corp_code ,
    'pblntf_ty' : 'A',
    'bgn_de' : '20230101' ## 사업보고서 시작일!
}

response = requests.get(url_json, params = params)
res = response.json()
if res ['status'] =='013' :
    print(f'{i},{corp_code}, {corp_df.loc[i,"corp_name"]}, 사업보고서개수 : 0')
    
df_imsi = pd.DataFrame(res['list'])
print('==================== 보고서 목록 ====================')
print(df_imsi)


# API로 데이터 가져오기
# ====================================================================================================
# ====================================================================================================
url = 'https://opendart.fss.or.kr/api/document.xml'
params = {
    'crtfc_key': api_key,
    'rcept_no': '20230307000542',
}

r = requests.get(url, params=params)

## 가져온 데이터를 XML 기반 파싱
try:
    tree = ET.XML(r.text)
    status = tree.find('status').text
    message = tree.find('message').text
    if (status != '000') & (status != '014') :
        raise ValueError({'status': status, 'message': message})

        
    
except ET.ParseError as e:
    pass

zf = zipfile.ZipFile(io.BytesIO(r.content))
info_list = zf.infolist()
fnames = sorted([info.filename for info in info_list])
## 결과물을 리스트에 넣기
xml_text_list = []
for fname in fnames:
    xml_data = zf.read(fname)
    try:
        xml_text = xml_data.decode('euc-kr')
    except UnicodeDecodeError as e:
        xml_text = xml_data.decode('utf-8')
    except UnicodeDecodeError as e:
        xml_text = xml_data
    xml_text_list.append(xml_text)

print('==================== 파일 확인/ 파일 내용 확인(xml원문) ====================')
print(fnames)
print(xml_text_list[0])


# (예시) 사용의 내용. 부분만 파싱
# ====================================================================================================
# ====================================================================================================
xml_text = xml_text_list[0]

# 리스트 슬라이싱
business_res = xml_text[xml_text.find('II. 사업의 내용</TITLE>'):xml_text.find('III. 재무에 관한 사항</TITLE>')]
print('==================== II. 사업의 내용</TITLE> 부분만 확인 ====================')
print(business_res)


