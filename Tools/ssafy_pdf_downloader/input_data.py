# 입력 보안을 위함
import getpass

info = '''
시작 및 종료주차 관련
    edussafy login session이 간헐적으로 종료되는 경우가 존재함.
    start_week와 end_week를 같게 처리하여 해결.
    session 유지가 가능하면 end_week = int(input('xxx').strip())로 변경하면 코드 그대로 작동함.
'''

class User:
    def __init__(self, id, pwd):
        self.id = id
        self.pwd = pwd


class Week:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.now = start


class Command:
    def __init__(self, day_only, is_merge):
        self.day_only = day_only
        self.is_merge = is_merge


# ======================================== login data 설정 --------================================
# 로그인 정보입력 함수
def get_data():
    user_id = input('edussafy_id: ')
    user_pwd = getpass.getpass('eddussafy_password: ')
    user = User(user_id, user_pwd)

    # 다운로드 할 주차별 정보
    start_week = int(input('다운로드를 진행할 추차: ex. 12주차면, 12 <------를 입력하시면 됩니다 ^^: ').strip())
    end_week = start_week
    week = Week(start_week, end_week)
    
    # 명령 정보
    day_only = int(input('전체 요일을 다운로드 하려면 0, 특정 요일을 다운로드 하려면 1~5사이 입력. ex. 수요일이면 3 <------를 입력하시면 됩니다 ^^: '))
    is_merge = ''
    if day_only:
        is_merge = input('pdf 병합본을 생성여부 Y/N:').strip().upper()
    command = Command(day_only, is_merge)
    return user, week, command
####################################################################################################
####################################################################################################

if __name__ == '__main__':
    print(info)