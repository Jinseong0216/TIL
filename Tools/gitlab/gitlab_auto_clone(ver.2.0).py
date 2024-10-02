from os import path
from time import sleep
from platform import system
from getpass import getpass
from subprocess import run
from requests import get

SEPERATOR=['hw','ws']
STAGE=[['2','4'], ['1','2','3','4','5','a','b','c']]

os_nlst={'Windows':1, 'Darwin':2, 'Linux':3, 'Ubuntu':4, '':5}  # 운영체제 정보 가져오기
sc={'!':'%21','#':'%23','$':'%24','&':'%26',"'":'%27','(':'%28',')':'%29','*':'%2A','+':'%2B',  # 리눅스 사용자 클론 시 비밀번호에 특수문자가 존재할 경우
    ',':'%2C','/':'%2F',':':'%3A',';':'%3B','=':'%3D','?':'%3F','@':'%40','[':'%5B',']':'%5D'}  # 에러 방지 위해 URL인코딩 사용
glst=['windows','macos','visualstudiocode','pycharm','python','django','flask','vuejs','database']  # gitignore 생성 기본값
lst=['linux','eclipse','intellij','java','c','c++','go','dart','flutter']  # gitignore 추가 생성값
gitignore=''  # 생성될 gitignore 문자열


def set_ignore(p=0):  # gitignore 문자열 받아오기
    global gitignore
    alst=[]
    
    if p==0:
        print()
        for i in range(len(lst)):
            print(i+1, lst[i], end='\t')
            if (i+1)%4==0:print()
        print()
        d=input("\n추가할 속성의 번호를 선택해 주세요.(구분자 공백 사용) : ").split()
        for di in d:alst.append(lst[int(di)-1])
    gurl='https://www.toptal.com/developers/gitignore/api'
    print('\ngitignore 생성중입니다......\n')
    gitignore=get(f'{gurl}/{",".join(glst+alst)}').text


def ignore(folder):
    with open(f'./{folder}/.gitignore', 'w', encoding="UTF-8") as f:
        f.write(gitignore)
        print(f"{folder}에 gitignore 파일 생성")
    f.close()


def file(i=0):  # 설정 파일 읽기/쓰기/변경; 기본값 설정 생성or읽기
    if i==1:
        with open('clone.ini', 'w', encoding="UTF-8") as f:
            user=input("\n깃랩 사용자 이름을 입력해주세요. : ")
            sub=input("과목명을 입력해주세요. (ex> django, js...) : ")
            f.write(user+'\n')
            f.write(sub+'\n')
        f.close()
        print("\n변경 완료.\n")
    else:
        try:
            with open('clone.ini', 'r', encoding="UTF-8") as f:
                user=f.readline()
                sub=f.readline()
        except:
            with open('clone.ini', 'w', encoding="UTF-8") as f:
                user=input("\n깃랩 사용자 이름을 입력해주세요. : ")
                sub=input("과목명을 입력해주세요. (ex> django, js...) : ")
                f.write(user+'\n')
                f.write(sub+'\n')
        f.close()
    return user.strip(), sub.strip()


def clone(USER_NAME, SUBJECT, OS_N):  # 깃랩 레포 클론하기
    run(clear, shell=True)
    print(f"\n{USER_NAME}의 {SUBJECT} 레포 관리\n")
    base_URL='https://lab.ssafy.com' if OS_N<=2 else f'https://{USER_NAME}:{"".join(sc[a] if a in sc else a for a in getpass("깃랩 비밀번호를 입력해주세요. (화면에 노출 X): "))}@lab.ssafy.com'
    DAY=input("프로젝트 차수 입력 (ex>  2차. Templates ==> 2): ")
    
    print("\n.gitignore 기본 세팅\n")
    print(*glst)
    x=input("\n.gitignore에 추가할거 있나요? (일회성, 넘기려면 enter) (Y/y)")
    if x=='Y' or x=='y' or x=='ㅇ' or x=='o' or x=='ㅇㅇ':set_ignore()
    else:set_ignore(1)
    run(clear, shell=True)
    
    for sep in range(2):
        for st in STAGE[sep]:
            PROJECT=f'{SUBJECT}_{SEPERATOR[sep]}_{DAY}_{st}'
            print(f'\n{PROJECT} 클론 시도중...')
            
            URL=f'{base_URL}/{USER_NAME}/{PROJECT}'
            folder_path=f'./{SUBJECT.upper() if SUBJECT == "js" else SUBJECT.capitalize()}_{DAY.zfill(2)}/{PROJECT}'
            cmd=f'git clone {URL}.git {folder_path}'
            output=run(cmd, shell=True, capture_output=True, text=True)
            
            if output.returncode==0:
                print(f'{PROJECT} 클론 성공.')
                if not path.exists(f'{folder_path}/.gitignore'):ignore(folder_path)
            elif output.returncode==128:
                if 'denied' in output.stderr: print("권한 거부 당함.... 비번 틀렸을수도...?")
                else: 
                    print(f'{PROJECT} 폴더가 이미 존재합니다.')
                    if not path.exists(f'{folder_path}/.gitignore'):ignore(folder_path)
            else:print('무슨 문제일까요...? 알려주세요...\n', output, '\n')


def del_dot_git(USER, SUBJECT, OS_N):
    x=input("\n실습 진짜로 다함? (Y/y)")
    if x=='Y' or x=='y' or x=='ㅇ' or x=='o' or x=='ㅇㅇ':
        run(clear, shell=True)
        del_co= 'rmdir /s /q' if OS_N==1 else 'rm -rf'
        
        try:
            print(f"\n{USER}의 {SUBJECT} 레포 관리\n")
            DAY=input(f"\n{SUBJECT} 프로젝트 차수 입력 (ex>  2차. Templates ==> 2): ")
            
            for sep in range(2):
                for st in STAGE[sep]:
                    PROJECT=f'{SUBJECT.upper() if SUBJECT == "js" else SUBJECT.capitalize()}_{DAY.zfill(2)}/{SUBJECT}_{SEPERATOR[sep]}_{DAY}_{st}'
                    folder_path = f'"{PROJECT}/.git"'
                    print(f'\n{folder_path} 삭제 시도중...')
                    cmd=f'{del_co} {folder_path}'
                    output=run(cmd, shell=True, capture_output=True, text=True)
                    
                    if OS_N==1:
                        if output.returncode==0:print(f'{folder_path} 폴더가 삭제되었습니다.')
                        elif output.returncode==2:print(f'Error: {folder_path} 폴더를 찾지 못했습니다. 이미 삭제되었을 수도?')
                    else:print(f'{folder_path} 폴더가 삭제되었습니다.')
        except:
            print("경로 없어용.....")
    else: print('\n다하고 오세요~')


def exit():
    print("\n프로그램을 종료합니다.\n")
    sleep(2)


if __name__=='__main__':
    print("\n주의 >> 실행파일과 동일 경로상에서 동작됩니다.")
    print("주의 >> 리눅스 사용자는 클론 시 살짝 위험할수도...?")
    print("주의 >> 실습실 생성은 다 하셨죠...?\n")
    
    os_n=os_nlst[system()]  # 운영체제 정보 가져오기
    if os_n==5:print('운영체제 뭐쓰세요...? 정보가 없는데요....')
    clear = 'cls' if os_n==1 else 'clear'  # Windows에선 cls Mac/Linux에서는 clear
    sleep(2)
    u,su=file()  # 사용자 정보 등록/가져오기
    
    while 1:
        try:
            run(clear, shell=True)
            print(f"\n{u}의 {su} 레포 관리\n")
            s=int(input("1. GITLAB clone  2. Del .git  3. Modify Settings (exit : 0): "))
        except:
            print("\n정수만 입력해주세요.")
            sleep(2)
            continue
        if s==0:
            exit()  # 종료
            run(clear, shell=True)
            break
        if s==1:
            print()
            clone(u, su, os_n)  # 깃랩 클론 따오기
            input("\n종료하려면 엔터를 눌러주세요.")
            exit()
            run(clear, shell=True)
            break
        elif s==2:
            print()
            del_dot_git(u, su, os_n)  # git 설정 폴더 삭제
            input("\n종료하려면 엔터를 눌러주세요.")
            exit()
            run(clear, shell=True)
            break
        elif s==3:
            u,su=file(1)  # 사용자 정보 수정
            sleep(2)
            run(clear, shell=True)
        else:
            print("\n1, 2, 3 중 하나만 입력해주세요.\n")
            sleep(2)
            continue
