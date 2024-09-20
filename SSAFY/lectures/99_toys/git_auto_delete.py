# 자동으로 .git을 삭제하는 코드
# 지금은 연습중이라서 최상단 폴더에 .git 없지만..
# 나중에 실제 git으로 관리하는 폴더에는
# 이 코드가 있는 위치에 .git이 있을것이다.
    # 그러므로 root 폴더의 .git 제외하고
# 나머지 폴더의 모든 .git 삭제
import os
import subprocess

current_folder = os.getcwd()
print(current_folder)
# 현재 폴더의 모든 하위 폴더를 반복
for foldername, subfolder, filenames in os.walk(current_folder):
    # print(foldername, subfolder, filenames)
    # root 디렉토리는 제외
    if foldername == current_folder: continue
    folder_path = os.path.join(foldername, '.git')
    subprocess.run(['rm', '-rf', folder_path])
    print(f'{folder_path} 폴더가 삭제 되었습니다.')
