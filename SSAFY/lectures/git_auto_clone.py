import os
import subprocess

current_folder = os.getcwd()
print(current_folder)

'''
    
    https://lab.ssafy.com/dnjsrua0514/django_hw_1_2
    https://lab.ssafy.com/dnjsrua0514/django_hw_1_4
    코드를 쓴다 -> 반복문을 쓸 수 있다.
    똑같은 일을 반복해서 시킬 수 있다.
'''
USER_NAME = 'dh0728'
SUBJECT = input('과목을 입력해 주세요. ex) django, db, js, vue : ')
DAY = input('날짜를 입력해 주세요. : ')
# SEPERATOR = 'hw'
# STAGE = '2'
for sep in ['hw', 'ws']:
    # 만약, sep -> hw이면 2, 4만 순회
    # 만약, sep -> ws이면 1 ~ c까지 순회
    for stage in [1, 2, 3, 4, 5, 'a', 'b', 'c']:
        BASE_URL = f'https://lab.ssafy.com/{USER_NAME}/{SUBJECT}_{sep}_{DAY}_{stage}'
        subprocess.run(['git', 'clone', BASE_URL])
# print(BASE_URL)