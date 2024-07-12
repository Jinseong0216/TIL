# 07/11(목) 수업내용 정리

## 공지사항 
- 앞으로 알고리즘 수업 진행시, 발표 위주로 수업을 진행 할 예정
- 파이썬 시험 어렵게 출제할 예정
- 오늘 수업내용을 markdown 문법을 이용하여 정리
    - 내일 업로드 할 예정


## Markdown
- 문서를 만드는 데 특화된 언어

- Heading
    - \# Heading 1 혹은 \<h1> Heading 1 \</h1>
    - \## Heading 2 혹은 \<h2> Heading 2 \</h2>
    - ...
    - \##### Heading 5 혹은 \<h5> Heading 5 \</h5>


-  서식 만들기
    - \- 을 통해 순서가 없는 서식 만들 수 있음
        - 순서가 없는 서식
        - 순서가 없는 서식
    - Num. 을 통해 순서가 있는 서식 만들 수 있음
        1. 순서가 있는 서식
        2. 순서가 있는 서식

- Code Block 사용가능
    - \```언어이름   코드 ```
        ```python
        print("hello")
        print("world")
        ```
    - 문장 내부에 코드 사용 \` 코드 \`
        - 파이썬은 `print`함수를 사용해 텍스트를 출력한다.

- 주소 & 이미지의 링크사용하기
    - [이름]\(url)

        - [구글](https://google.com)

        - [Naver](https://naver.com)

        - [이미지](https://picsum.photos/200/300)

- 텍스트 관련 기능
    1. 굵은 글씨 사용하기(\*\*글자\*\*)
        - **나는**
        - 나는
    2. 기울이기(\*글자\*)
        - *나는*
        - 나는
    3. 취소선(\~~~글자\~~~)
        - ~~취소선~~
        - 취소선
    4. 수평선(\***)
        - *** 


## CLI(Command Line Interface)
- GUI와 CLI방식의 차이
    - 마우스 클릭을 통해 C 드라이브 → user 등으로 들어가는 방법이 GUI방식
    - cmd에서 cd ... 주소를 쳐서 들어가면 CLI방식

- 앞으로 CLI를 사용 할 때, cmd보단 git bash를 사용 할 예정

- CLI를 사용해야하는 이유
    1. 키보드만으로 모든 작업 가능
    2. 여러 환경에서 사용가능
    3. 메모리등 적게 소모
    4. CLI명령은 GUI명령보다 더 섬세한 작업이 가능함

- 명령어
    - `clear`
    - git bash에서 cd(change directory)를 통해서 주소를 변경하고자 할 경우
    - `cd 폴더명` 으로 변경가능
        - 폴더명에 공백이 있으면 \'' 사용해야함
            
            Ex) ‘새 폴더’
            
    - `cd ../..` 으로 한번에 디렉토리 두 칸을 올라갈 수 있음
    - `cd layer1/layer2`로 한 번에 디렉토리 두 칸을 내려갈 수 있음
    - `cd ../layer2_2` 같은 방식도 가능함

    - `ls`를 통해 git bash에서 같은 디렉토리에 있는 파일을 확인 가능함
        - `ls -a`로 숨긴파일까지 다 볼수 있음

    - git bash에서 .은 현재 디렉토리를 의미

    - `mkdir`(make directory)로 새 디렉토리 생성가능

    - `touch 파일명`
        - 파일생성
        - ex) touch a.txt
    - `rm 파일명` 
        - 파일삭제
        - 디렉토리 삭제는 rm -r
    - `start`를 통해서 파일 실행가능

    - code를 통해서 파일을 code로 실행가능
        - `code .`을 통해서 현재 디렉토리에서 code로 실행도 가능

    - `pwd`를 통해서 절대경로를 알 수 있다

        - CLI에서 나의 경로를 아는 것이 가장 중요
    
            상대경로와 절대경로의 차이를 알기
    
- git bash에서 팁: cd D + Tap 치면 cd Desktop으로 바뀜
    
    (D로 시작하는 파일혹은 폴더가 하나인 경우)
    
    (cd De + Tap 해도 됨)
    

**파일명 주의사항**
- 한글사용X
- 공백사용X
- 단어와 단어 사이에 _ 사용하기


## Git (분산 버전 관리 시스템)
    
- 버전관리
    - 변화를 기록하고 추적하는 것
    - 문제가 생겼을 때 롤백하여 복구 할 수 있는 장점이 있다
    
    - 중앙 집중식 vs 분산식
        - 분산식 : 버전을 여러 개의 복제된 저장소에 저장 및 관리
        - 분산 구조의 장점
            - 중앙서버 의존하지 않고 동시에 다양한 작업가능
            - 백업 복구 용이
            - 인터넷에 연결되지 않아도 가능
                - 나중에 중앙 서버와 동기화 시키면 됨
    

- 최종완성버전 / 변경사항들로 관리하면서 효율적인 버전 관리를 가능하게 함

- git의 3가지 영역
    - Working Directory
        - 실제 작업 중인 파일들이 위치하는 영역
    - Staging Area
        - working directory에서 변경된 파일 중,
            
            다음 버전에 포함시킬 파일들을 선택적으로 추가하거나 제외할 수 있는 
            
            **중간 준비 영역**
            
    - Repository
        - 버전 이력과 파일들이 **영구적**으로 저장되는 영역
            
            모든 버전과 변경 이력이 기록됨
            

- git의 명령어 / 관련 용어
    - commit: 변경된 파일을 저장하는 행위
        - (commit지점 = 일종의 롤백 포인트)
    
    - `git init`: 로컬 저장소 설정(초기화)
        - git의 버전 관리를 시작할 디렉토리에서 진행
    
    - `git add`
        - 변경사항이 있는 파일을 staging area에 추가
        - git add a.txt
        - git add layer2_1
        - git add a.txt,b.txt
        - git add *.txt 확장자가 txt인 모든 파일이 staging area에 추가
        - git add . 으로 모든파일추가 가능
        
    - `git rm -- catched  파일명`
        - staging area에 올린 파일을 다시 working area로 내리는 것
        
    - `git commit`
        - staging area에 있는 파일들을 저장소에 기록
            
            즉, 해당 시점의 버전을 생성하고 변경 이력을 남기는 것
            
        - `git commit -m '메세지'` 명령어를 통해서
            
            내가 이번 파일을 저장소에 기록하는 이유도 함께 추가할 수 있다

    - **commit 코멘트 수정하기**
        1. 해쉬값 확인(online으로 불러오는게 편함)
        2. `git commit --ammend` 
        3. I눌러 insert 들어가기(편집모드)
        4. 편집하기
        5. exc (커맨드모드 들어가기) 
        6. :wq (나가기)
        7. `git log --online`
            - 다른 것은 다 같으나 해시값이 바뀐 것을 알 수 있음

    - **특정 파일은 제외하고 commit한 경우 수정하기**
        1. 해당파일을 add함
        2. `git commit --amend`
        3. I눌러 insert 들어가기(편집모드)
        4. 코멘트도 편집한번 해주고(선택)
        5. exc
        6. :wq
            
    - `git status`
        - 각 파일들의 상태 확인이 가능
        - Working Area, Staging Directory의 정보만 확인이 가능함
            
            즉, Repository의 정보는 확인 할 수 없다
        - 커밋된 파일을 수정하고 status를 입력하면 수정 되었음을 확인 할 수 있다
            수정된 파일은 다시 add해야 커밋이 가능
            
    - git commit -m”OOO” 에러난 경우
        - `git config --global user.email "이메일 주소"`
        - `git config --global user.name "이름"`
            - 여기서 global로 설정을 했기 때문에 앞으로는 에러 안날 것
        - 다시 git commit -m ‘first commit’
        - 즉, commit을 생성하기 위해서는 작성자의 정보(메일주소, 유저네임)이 필요함
    - `git log`
        - 커밋의 해시번호와 만든 시점, author가 남긴 메세지, 이메일확인가능
            Repository에 적용되는 명령어
        - git log --oneline
            -간단하게 볼 수 있음
    - `git config --global -l`
        - git global의 설정정보 보기

- <span style ="color.red"> **git init 주의사항** </span>
    - 로컬 저장소내에 다시 로컬 저장소를 만들지 말 것
    - git 저장소 안에 git 저장소가 있을 경우 가장 바깥 쪽의 git 저장소가 
        안쪽의 git 저장소의 변경사항을 추적 할 수 없기 때문
    - 특히, 상위 디렉토리에 git 저장소를 만들면 안됨
    
- **해결방법**
    - 하위 디렉토리에 해당하는 git 저장소에서 .git 폴더를 제거하면 됨
        - rm -r .git

## GitHub
- GitHub TIL시작하기 등, 검색하여 참고
