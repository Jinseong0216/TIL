## 09/20 수업내용 정리

### 지난 기억할 내용
- django-admin startproject firstpjt .
- python manage.py runserver
- python manage.py startapp articles
  - 이후에 앱을 등록해야함(setting.py에서 Installed_Apps)
```python
# articles/models.py

class Article(models.Model):
    # ModelField = DB의 테이블 열을 나타내는 구성 요소
    # Data의 유형, 제약조건을 정의

    # CharField는 명명규칙만 봐도 Class임을 알수 있음.(max_length<- 초기값)
    title = models.CharField(max_length=10)
    content = models.TextField()
    # auto_now_add = 데이터가 처음 생성될 때만, 자동으로 현재 날짜시간을 저장
    created_at = models.DateTimeField(auto_now_add=True)
    # auto_now = 데이터가 저장될 때마다 자동으로 현재 날짜시간을 저장
    updated_at = models.DateTimeField(auto_now=True)
```

- Django 공부할 때, 공식문서 활용[https://docs.djangoproject.com/ko/5.1/]
  - 목차 보면서 step by step으로 읽어보기.
  - 최신버전 5.2 우리는 4.2사용 중. Version 변경 후 문서 읽기 권장.

***
### Django - Model Field

- **Field**(sql에서 attribute와 같음)
1. `CharField()`: OOO
2. `TextField()`: 길이 제한이 없는 대용량 텍스트를 저장하기 위함.(실제 제한이 없는 것은 아님. 시스템 마다 상이함.)

- **Field Options**(자주 사용하는 옵션들)
1. null: DB에서 Null값을 허용할 지 결정(기본 값: False)
2. black: form에서 빈 값을 허용할 지 결정(기본 값:False)
3. default: 필드의 기본값을 설정

- **어떻게 적용할 것인가?**
    - models.py에서 클래스를 생성하거나 수정하였을 경우, 아직 DB에 반영되지는 않았음(build해야함)
    - db.sqlite3에 반영해야함
    - models class(설계도 초안) $\rightarrow$ `makemigrations` $\rightarrow$ migration 파일(최종 설계도) $\rightarrow$ `migrate` $\rightarrow$ db.sqlite3(DB)

    - **makemigrations**
      - migrations 디렉토리 안의 .py파일의 내용이 변경됨
      - 결과창 
        - Create model Article(최초 실행시)
        - Remove field updated_at from article(`updated_at = models.DateTimeField(auto_now=True)`를 주석처리한 결과)
        - Add field updated_at to article(주석을 해제한 결과)
      - 터미널 결과
        ```
        $ python manage.py makemigrations
        Migrations for 'articles':
            articles\migrations\0002_remove_article_updated_at.py
            - Remove field updated_at from article
        ```
    
    - **migrate**
        - 터미널 결과
        ```
        $ python manage.py migrate
        Operations to perform:
        Apply all migrations: admin, articles, auth, contenttypes, sessions
        Running migrations:
        Applying articles.0002_remove_article_updated_at... OK
        Applying articles.0003_article_updated_at... OK
        Applying articles.0004_article_test_updated_at... OK
        Applying articles.0005_remove_article_test_updated_at... OK
        ```

### DB관리
  1. DB확장프로그램 설치후(이름: ...)
  2. VScode 왼쪽의 DATABASE들어가서
  3. CREATE Connection누르고
  4. SQLite누르기(장고의 디폴트는 SQLite. 다른것도 가능한듯)  
    SQLite - 물리적으로 저장이된다는 특징이 있음.
  5. DatabasePath에 db.sqlite3 파일을 등록하고 connect누르기(성공 시)
    ```
    2024-09-20 09:09:30 [DEBUG] Resource server started on port 8828
    2024-09-20 10:08:40 [DEBUG] Creating SQLite connection for 1726794520647
    2024-09-20 10:08:40 [ INFO] Start downloading sqlite3.exe...
    2024-09-20 10:08:41 [ INFO] Download success!
    ```
  6. 이후에, DATABASE에 들어가면 볼수 있음.(테이블이 생성됨)  
    테이블 명명 규칙: 앱이름_클래스이름.

  - **이미 생성된 테이블에 필드를 추가해야 한다면?**
    - **주의사항** 빈값으로 새로운 필드를 추가 안됨.(데이터 무결성 관련)
    - makemigrations, migrate 해주면 됨.
  
    ```
    $ python manage.py makemigrations
    It is impossible to add a non-nullable field 'test_field' to article without specifying a default. This is because the database needs something to populate existing rows.
    Please select a fix:
    1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
    2) Quit and manually define a default value in models.py.
    Select an option:
    ```
      - 2가지 선택 사항을 제공해줌(보통 1번을 선택함)
       - 1번) 기본 값으로 넣을게
       - 2번) 나가서 기본 값을 설정하고 오겠다.
         - 1번 선택시!!!
          ```
          Please enter the default value as valid Python.
          The datetime and django.utils.timezone modules are available, so it is possible to provide e.g. timezone.now as a value.
          Type 'exit' to exit this prompt
          ```
          - 유효한 파이썬 문법으로 적어달라는 의미(만약, 엔터치면 알아서 넣어줌 .timezone으로)
          - (나는 .timezone 그냥 입력했음. )
    - 이후에, migrations안의 .py를 통해서 dependency를 보면서 의존관계 체크가 가능함!!! (옛 설계 파일이라고 지우면 의존성에 의해 꼬일 수 있음)

### Automatic admin interface
- Django가 추가 설치 및 설정 없이 자동으로 제공하는 관리자 인터페이스
  - 데이터 확인 및 테스트 등을 진행하는데 매우 유용

- Django는 기본적으로 관리자 기능에 대해 제공해줌.(보통 잘 없어서 좀 편한듯.)

1. admin 계정 생성
   - email은 선택사항이기 때문에 입력하지 않고 진행 가능
   - 비밀번호 입력시 보안상 터미널에 출력되지 않으니 무시하고 입력 이어가기
  
  입력: `python manage.py createsuperuser` $\rightarrow$  출력: `Username (leave blank to use 'ssafy'):`
  보통: admin 사용. 입력하면 `Email address:` 출력되는데 엔터 눌러서 블랭크 사용가능
  `Password: ` 만약 1234 입력시. 경고 + 바꿀건지 선택지를 줌.

  auth_user에 관리자 계정이 생성됨.

- **주의사항**
  - migration을 한 번도 안하고 관리자 계정을 만들면 저장될 테이블이 없기 때문에 관리자 계정이 생성되지 않음!
  
- 이제 http://127.0.0.1:8000/admin/에서 로그인 가능해짐

- 그러나 왜 아직까지, article class가 안보일까?
  - 현재 디렉토리의 models모듈에서 Article 디렉토리 등록 하고 코드 입력
  ```
  from django.contrib import admin
  from .models import Article 

  # Register your models here.
  # admin site에 등록한다.
  admin.site.register(Article)
  ```
  - 저장한 후 http://127.0.0.1:8000/admin/에서 로그인해보면 바로 Articles를 볼수 있음.
  - 우측 상단에 Add article을 할수 있음.
  - 그러나.. 기존에 등록 했던 id, created_at, updated_at은 보이지 않는다.(장고가 자동으로 등록해주기 때문.)
  - 들어가서 Title과 Content에 값을 등록하려고 보면
  - Title과 Content의 입력칸이 다름. 왜? 제약조건을 미리 지정했기 때문.
  - 등록한 후, DataBase에 들어가보면 articles_article에 새로운 instance가 생성된 것을 확인 할 수있음.
  - admin사이트에서 수정, 삭제 또한 가능함.
  

- **간혹 데이터베이스 복구해야하는 경우 그냥 초기화 하는게 편함**

### 데이터베이스 초기화
- **간혹 데이터베이스 복구해야하는 경우 그냥 초기화 하는게 편함**

1. migrations 내부의 파일 삭제(init제외)
  - ex. 0001_initial.py or 0002_article_crated_at_article_updated_at.py 이런것들...
  
  - _init_.py 지우면 안됨
  - migrations 폴더 자체를 지우면 안됨

2. db.sqlite3 파일 삭제

### Migrations 기타 명령어
1. `python manage.py showmigrations`
   - 현재 각 설계도의 migrate상태를 확인해줌!
   - **X는 migrate안된 것이 아니라, 했다고 체크 한 것임**
   - 
2. `python manage.py sqlmigrate articles 0001`
   - 해당 migrations 파일이 sql언어로 어떻게 번역되어 DB에 전달되는지 확인하는 명령어
  
3. 첫 migrate시 출력 내용이 많은 이유
   - 기본적으로 Django 프로젝트가 동작하기 위해 미리 작성 되어있는 기본 내장 app들에 대한 migration 파일들이 함께 migrate 되기 때문

### SQLite
- DB관리 시스템 중 하나이며, Django의 기본 데이터베이스로 사용됨
- 물리적 파일이 존재함!
- 가벼움!
- 호환성이 좋음!
- 보통 모바일 환경에서 사용함.

## 강사님 수업.

### vscode 단축키
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <!-- 거의 대부분의 TEST EDITOR에서 사용 가능(아마). -->
    <!-- ctrl + 좌우: 공백기준 커서 위치 옮기기 -->
    <!-- ctrl + shift + 좌우: 공백기준 드래그 -->
    <!-- alt + shift: 현재 커서 위치 라인 복제 -->

    <!-- ctrl + d: 현재 드래그(포커싱된) 문자열과 일치하는 문자열 같이 포커싱 -->

    <!-- ctrl + alt + 위아래방향키: 커서 증식 -->
    <!-- ctrl + tap: 현재 활성화된 탭 위치 바꾸기 -->
    <!-- ctrl + b: explorer -->
    <!-- ctrl + alt + 좌우방향키: 해당위치로 탭 옮기기-->
    <!-- ctrl + w: 탭 종료 -->
    <div class="box item color test"></div>
    <!-- alt + 위 아래 방향키: 포커싱 옮기기 -->
    
    
    <!-- ctrl + c: 복제 -->
    <!-- ctrl + x: 잘라내기 -->


    <!-- ctrl + Tap + `: 새 터미널 생성 -->
    <!-- ctrl + `: 터미널 열고 닫기(새 터미널 아님!) -->

    
    <!-- vscode 단축키 x html emmet -->
        <!-- emmet은 선택자를 쓰면 된다. -->
        <!-- ul.box-item{$}*10 + Tap-->
            <ul class="box-item">1</ul>
            <ul class="box-item">2</ul>
            <ul class="box-item">3</ul>
            <ul class="box-item">4</ul>
            <ul class="box-item">5</ul>
            <ul class="box-item">6</ul>
            <ul class="box-item">7</ul>
            <ul class="box-item">8</ul>
            <ul class="box-item">9</ul>
            <ul class="box-item">10</ul>

        <!-- ul.box_item*10 + Tap -->
        <ul class="box_item"></ul>
        <ul class="box_item"></ul>
        <ul class="box_item"></ul>
        <ul class="box_item"></ul>
        <ul class="box_item"></ul>
        <ul class="box_item"></ul>
        <ul class="box_item"></ul>
        <ul class="box_item"></ul>
        <ul class="box_item"></ul>
        <ul class="box_item"></ul>
</body>
</html>
```
### 간이로 배포하는 법
Render를 통해서도 할수 있음.
