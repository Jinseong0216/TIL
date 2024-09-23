## 09/23 수업내용 정리
- 기억할 내용(복습 및 오늘 내용)
  - 명시적 상대경로
      - `from . import views`
  - include 이해하기
  - 공식문서 검색할 때, 구글을 통해서 들어가는 것이 훨씬 좋음

### 라이브강의에서의 주의사항
  1. 테이블.id 사용 X **테이블.pk 권장**
  2. **create 방식 사용 X**
   
### 아래의 순서 요약
  1. 기본 셋팅(가상환경, 기존의 패키지(Django, ... etc))
  2. `pip install ipython`
  3. `pip install django-extensions`
  4. settings.py에 `django_extensions` (installed app에)를 추가
  5. `pip freeze > requirements.txt`(선택)
  6. 마이그레이션 진행
  7. `python manage.py shell_plus`를 통해 Django shell 실행 후, 테이블 추가 등의 작업

#### ORM
- Django와 DB간 사용하는 언어가 다르기 때문에 소통이 불가능함. 이를 해결하기 위한 것이 ORM(장고에 이미 내장되어 있음.)
  
#### QuerySet API
- ORM에서 데이터를 검색, 필터링 및 정렬하는데 사용하는 도구임.

##### QuerySet API의 구문
- Article.objects.all() = Model_class.Manager.QuerySet_API의 의미임
    - Article.objects.all()(Python Object에서 명령) $\rightarrow$ 전체 게시글을 줘 $\rightarrow$ 전체 게시글을 받아(DB에서) $\rightarrow$ QuerySet(전체 게시글 데이터 전송) 

##### Query
- 데이터 베이스에 특정한 데이터를 보여 달라는 요청
- 쿼리문을 작성한다.
- 파이썬으로 작성한 코드가 ORM에 의해, SQL로 변환되어 데이터베이스에 전달되며, 데이터베이스의 응답 데이터를 ORM이 QuerySet이라는 자료형태로 변환하여 전달해줌.
- 데이터베이스에게서 전달 받은 객체 목록(데이터 모음), 순회가 간으한 데이터로써 1개 이상의 데이터를 불러와 사용할 수 있음
- Django ORM을 통해 **만들어진 자료형**
- 단, DB가 단일한 객체를 반환 할 때는 QuerySet이 아닌 모델(Class)의 인스턴스로 반환됨

##### QuerySet API는
- Python의 모델 클래스와 인스턴스를 활용해 DB에 데이터를 CRUD하는 것.(Create, Read, Update, Delete)


**주의 사항**
  - DB는 git에 올라가지 않음. 설계도만 올라감.
  - migrate 해주면 됨.


##### Django shell
- `pip install ipython` 해주면 이쁘게 나옴!!!! 아주 **편해짐**
  
- `pip install django-extensions`하고
- settings.py에 `django_extensions` (installed app에)를 추가 한 후,
- `python manage.py shell_plus`를 통해서 해당 위치에서 파이썬 쉘을 쓸 수있음
- 이후, 해당 쉘에서의 명령어를 넣으면 장고에 적용됨
- 입력하는 QuerySet_API 구문이 장고에 적용되는 것

##### Django shell 구문
- 데이터 객체를 생성하는 법(3가지)
- 아래의 방법으로 데이터 객체를 생성할 때, model에 정의된 Article 클래슬가 정의한 데이터 형식에 따라감

- 1번 방법
  - article = Article() # Article(class)로 부터 article(instance) 생성(이름에 유의)
  - article.title = '이름', 인스턴스 변수 title에 값을 할당
  - article.content = '값', 인스턴스 변수 content에 값을 할당
  - save를 호출해야 값이 저장됨 `article.save()`
  - `article`을 입력하면 해당 테이블의 PK를 알 수 있음
  - `article.id`를 통해 id를 확인가능
  - `article.pk`를 통해 pk를 확인가능. **권장**
  - **주의 사항 및 참고사항**
    - 전체 데이터를 조회 한 것임.(단일 X)
    - 여기까지 진행했으면, db.sqlite3에서 확인 가능함.(articles_article테이블이 생성됬음.)

- 2번 방법(초기값을 주면서 인스턴스를 생성)
  - article = Article(title = 'second', content='django!')
  - article하면 DB에 저장되어 있지 않음을 확인 가능
  - article.save()를 해줘야함
  - article을 해보면 이제 저장 된 것을 확인 가능
  - 이제 Article.objects.all()해주면 2개의 데이터가 있음을 확인 가능함

- 3번 방법(저장 이후, 바로 데이터를 생성하는 법)
  - Article.objects.create(title='third', content='django!')
  
- **save()**
  - 객체를 DB에 저장하는 인스턴스 메서드임
  
- **대표적인 조회 메서드**
  - Return new QuerySets
    - all() (전체 조회이기 때문에, 항상 쿼리셋을 줌. 데이터가 없더라도.)
    - filter() (조건)
  - Do not return QuerySets (쿼리셋이 아닌, **단일 객체**를 줌)
    - get()

  - all()
    - 전체 데이터 조회
    - `Article.objects.all()`
  - filter()
    - 주어진 매개변수와 일치하는 객체를 포함하는 쿼리셋 반환
    - ex. `Article.objects.filter(content='django!')`
    - 일치하는 객체가 하나라도 **단일 인스턴스가 아니라 쿼리셋을 줌!!!**
    - 결과가 없으면 빈 쿼리 셋을 줌. (<QuerySet []>)
  - get() 
    - 주어진 매개변수와 일치하는 객체를 반환
    - 조건에 맞는 결과가 없으면 에러
    - 주어진 결과에 일치하는 데이터가 **여러개라도 하나만 리턴**함
    - ex. `Article.objects.get(pk=1)`
    - 객체를 찾을 수 없으면 DoesNotExist 예외 발생
    - 둘 이상의 객체를 찾으면 MultipleObjectsReturned 예외 발생
    - 우의 특징으로 인해 **PK**와 같이 **고유성**을 보장하는 조회에서 사용해야 함

  - `article = Article.objects.filter(content=first')` 했을 때, 
  - `article[0]`을 해야 제대로 조회가 가능.(리스트와 같음)
  - `article[0].content`를 통해서 content속성 값 조회가능
  
- **Update**  
  - 인스턴스 변수를 변경 후 save 메서드 호출하면 됨!
  
- **Delete**  
  - 예시
  - article = Article.objects.get(pk=1)를 통해 호출하고
  - article.delete() 해버리면 바로 반영이 됨!
  - 만약 delete를 통해서 특정 데이터를 지웠다면 해당 데이터가 가지고 있던 id를 재활용 하지 않음
  - ex. pk가 0 1 2 3이 있는 테이블에서 pk=2를 지우고 새 데이터를 만들면 pk=4가 생김 
  - 이후에 pk=4를 지우고 새 데이터를 만들면 pk=5가 나옴
  
##### ORM with view
- Django shell에서 연습했던 QuerySet_API를 직접 view 함수에서 사용하기

- 지금까지 all, filter, get, create, save, delete를 배움

- **Field lookups**
  - **Django QuerySet API 문서 참조**
    - https://docs.djangoproject.com/en/4.2/ref/models/querysets/
      - gt/gte/lt/lte ... 등 자주 사용하는 메서드 내용 확인이 가능함
    - https://docs.djangoproject.com/en/4.2/topics/db/queries/
      - 어떻게 **쿼리를 만드는지 알려줌**! 일종의 가이드라인
      
  - 쿼리에서 조건을 구성하는 방법
  - 쿼리셋 메서드 filter, exclude, get 등에 대한 키워드 인자로 지정됨
  - Article.objects.filter(content__contains='dja')
    - content에 dja가 포함된 모든 게시글 조회
    - __contains(언더바 두개임)
  - Article.objects.filter(title__startswith='he')
    - title이 he로 시작하는 모든 게시글 조회

  - 여기에도 쿼리셋을 리턴하는 메서드/ 리턴하지 않는 메서드. **두 종류가 존재**함

- ORM, QuerySet API를 사용하는 이유
  1. 데이터베이스 추상화
    - 개발자가 특정 DB시스템에 종속되지 않고 일관된 방식으로 DB를 다룰 수 있음
  2. 생산성 향상
    - 복잡한 SQL쿼리를 직접 작성하는 대신 Python 코드로 DB작업을 수행할 수 있음
  3. 객체 지향적 접근
    - DB 테이블을 Python 객체로 다룰 수 있어, 객체 지향 프로그래밍의 이점을 활용할 수 있음.
- **전체 게시글 조회**를 하면서 연습해보자
- **단일 게시글 조회**를 하면서 연습해보자
  
  
  
  
    
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  