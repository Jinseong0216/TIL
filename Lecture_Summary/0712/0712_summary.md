# **07/12(금) 수업내용 정리**

## 공지사항
- 지금까지 공부한 내용들 정리하여 TIL형식으로 GitHUb에 업로드

***
- 오늘 할 내용
    - pull(이미 local에 있을 때)
    - clone(local에 없을 때)
    - remote repository
    - How to roll-back


## 원격 저장소
- 코드와 버전 관리 이력을 온라인 상의 특정 위치에 저장하여

    여러 개발자가 협업하고 코드를 공유할 수 있는 저장 공간

    원격 저장소 종류: **GitLab**(SSAFY에서 주로 사용), **GitHub**(Major), **Bitbucket**(Minor)


- **원격 저장소 만들기**
1. GitHub가입(repository를 main말고 master로 변경)
2. create repository
3. 로컬 저장소에 원격 저장소 추가
    - `git remote add origin remote_repo_url`
    - origin(추가하는 원격저장소 별칭)(일종의 convention)
    - remote_repo_url(원격 저장소 주소)
- **주의사항** 
    - terminal에서 Ctrl v 사용하지말고 shift insert 사용하기
    - add commit push 순서 항상 기억하기
    - 원격 repository에도 사실 .git폴더가 있어서 돌아가는 것임을 기억
- `git remote -v`
    - fetch 어디서 가지고 올것인가 의미
    - merge를 한번에 해주는 것이 
    - push(로컬 to 원격)
    - pull/clone(원격 to 로컬)
- `git push origin master`
    - 원격 저장소에 commit 목록을 업로드
    - git에게 origin이라는 이름의 원격 저장소에 master라는 이름으로 올려줘라는 의미
    - 입력하면 인증관리 창이 나옴(처음이라)
    - 권한 인증하면 됨
    - 이제 다시 내 github repository에 들어가면 
        기존에 commit했던 파일들이 올라가있는 것을 확인 할 수 있다.
    - GitHub에서 내용을 확인해보면 어떤 것들이 변경되었는지 알 수 있음.
        (코드 들어가서 보면 색,+기호 ... etc로 확인가능)

- **pull & clone**
    - `git pull origin master`
        -원격 저장소의 변경사항만을 받아옴
        - 이미 clone으로 받아온 경우, 사용하면 편함
    - `git clone remote_repo_url`
        - 원격 저장소 전체를 복제(다운로드)
        - 처음 repository를 받아오는 경우
        - clone으로 받은 프로젝트는 이미 git init이 되어 있음
        - **내가 git으로 관리되고 있는 디렉토리에 git clone해버리면 안됨**
            - git init 두 번 해버리는 것과 같음(원격 repo에도 .git이 있으므로)
        - desktop에서 git clone을 해버리면 first-repo폴더가 생김을 알 수 있음
            - git log로 확인해보면 이전의 변경사항들이 다 나옴을 알 수 있음 
    - `mv -f 기존이름 변경이름`
        - 폴더명 변경
    - 내 GitHub repository를 상대방과 공유하기 위해서는 아래의 내용이 전제되어야 함
        1. repository url을 상대방에게 제공
        2. 상대방의 email을 이용하여 초대 보내기
        3. 상대방의 승인
- **gitignore**
    - Git에서 특정 파일이나 디렉토리를 추적하기 않기 위해 사용
    - 한번에 여러 파일이나 디렉토리를 처리할 수 있음
    - `touch .gitignore` 하면 됨
    - `.gitignore` 이름으로 만들어야함.
        - 얘는 확장자가 없음
        - **git init 하기전에 미리 만들어야함!**
            
            방법은 있는데.. 귀찮고 권장하지 않음

            (git rm--cashed 같은 방법을 써야함)
        - gitignore 목록 생성 서비스
            - https://www.toptal.com/developers/gitignore/ 추천
            - Ex. Windows, Mac, Python를 쳐보면 알 수 있음
            - 나오는 내용을 전부 복사해서 .gitignore 파일에 넣으면 됨
- `git remote rm 원격_저장소_이름`
    - 현재 로컬 저장소에 등록된 원격 저장소 삭제
    - 원격 저장소 자체가 사라지는것이 아님. 연결이 끊기는 것
- `git revert commit_해시번호` (해시번호 앞에 4자리만 사용해도 됨)
    - 재설정
    - 단일 commit을 실행 취소 하는 것
    - 프로젝트 기록에서 commit을 없었던 일로 처리 후 그 결과를 새로운 commit으로 추가함
    
        이후, 해당 commit에 넣고자 하는 메세지를 입력하도록 vim편집기가 실행됨
    - 변경 사항을 안전하게 실행 취소 할 수 있도록 도와주는 순방향 실행 취소 작업
    - commit 기록에서 commit을 삭제하거나 분리하는 대신, 지정된 변경 사항을 반전시키는 새 commit을 생성
    - git에서 기록이 손실되는 것을 방지하여 기록의 무결성과 협업의 신뢰성을 높임
        
        즉, second commit에서 2.txt를 commit했는데 이를 취소해버리면
        
        commit된 2.txt는 사라지고 Revert second commit이 생기면서, commit된 2.txt파일이 사라짐
    - revert 추가 명령어는 찾아보기

- `git reset commit_해시번호` (해시번호 앞에 4자리만 사용해도 됨)
    - 되돌리기
    - 시계를 마치 과거로 돌리는 듯한 행위
    - 특정 commit으로 되돌아 갔을 때, 되돌아간 commit 이후의 commit은 모두 삭제
    - 아주 위험한 행위
    
    - Options
        - --soft
            -삭제된 commit의 기록을 staging area에 남김
        - --mixed
            - 삭제된 commit의 기록을 working directory에 남김(디폴트 값)
        - --hard
            - 삭제된 commit의 기록을 남기지 않음
        - --reflog
            - HEAD가 이전에 가리켰던 모든 commit을 보여줌
            - reset의 --hard 옵션을 통해 지워진 commit도 조회하여 복구 가능
- `git restore` 
    - Modified 상태의 파일 되돌리기 (Working Directory에서 적용되는 함수임)
    - Working Directory에서 파일을 수정한 뒤, 파일의 수정 사항을 취소하고, 원래 모습대로 되돌리는 작업
    - Ex. `git restore README.md`

- `git rm --cached` or `git restore --staged`
    - Staging Area에 올라칸 파일을 Unstage 하기
    - rm은 git 저장소에 commit이 존재하지 않는 경우 사용
    - restore는 git 저장소에 commit이 존재하는 경우 사용

- **GitHub Profile 꾸미기**
    - 알아서 구글링

- **TIL(Today I Learned)**        

- **문서화 연습의 중요성**
    - https://d2.naver.com/news/3435170 (refered from)

    - 개인적으로는 아래와 같이 개발자의 수준을 분류하고 싶습니다.

        레벨0: 이미 쓰고 있는 개발도구의 사용법을 알려주거나 가이드 문서를 줘도 잘 못 씀

        레벨1: 알려주거나 같은 팀에서 만든 가이드 문서에 있는 만큼만 쓸 수 있음

        레벨2:
        개발도구의 공식 레퍼런스를 보고 사용법을 스스로 익힐 수 있음
        자신이 경험한 사용법을 문서화해서 팀 내에 전파할 수 있음

        레벨3:
        여러 개발도구를 비교 분석해서 상황에 적합한 도구를 선택할 수 있음
        공식 레퍼런스 문서에서 부족한 부분을 수정해서 기여할 수 있음

        레벨4:
        개발도구의 문제를 소스 코드를 수정해서 Fork/패치해서 사용할 수 있음

        신입사원이라도 레벨2 정도는 함께 일할 개발자에게 기대를 하게 됩니다.

    - git 공식문서: https://git-scm.com/doc
    