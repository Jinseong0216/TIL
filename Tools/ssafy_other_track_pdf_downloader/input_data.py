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


class Track:
    target_course = 0
    def __init__(self, track):
        self.track = track

    @classmethod
    def select_course(cls, n):
        cls.target_course = n


class Command:
    def __init__(self, is_merge):
        self.is_merge = is_merge
        self.download_info = {
            'is_total_download': 'N', 
            'is_specific_download': 'N'
            }


# ======================================== login data 설정 --------================================
# 로그인 정보입력 함수
def get_user():
    user_id = input('edussafy_id: ')
    user_pwd = getpass.getpass('eddussafy_password: ')
    user = User(user_id, user_pwd)

    return user


# 명령 입력 함수
def get_command():
    # 다운로드 할 트랙 정보
    track_name = input('트랙 이름 or 키워드, ex. 파이썬, 자바전공, 자바비전공, 임베디드, 모바일, 데이터: ').strip()
    if track_name == '파이썬': track = '__파이썬__'
    elif track_name == '자바비전공': track = '__자바비전공__'
    elif track_name == '자바전공': track = '__자바전공__'
    elif track_name == '임베디드': track = '__임베디드__'
    elif track_name == '모바일': track = '__모바일__'
    elif track_name == '데이터': track = '__데이터 트랙__'
    track = Track(track_name)

    # 명령 정보
    is_merge = input('pdf 병합본 생성여부 Y/N: ').strip().upper()
    command = Command(is_merge)

    return track, command
####################################################################################################
####################################################################################################

if __name__ == '__main__':
    print(info)


