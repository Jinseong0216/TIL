## 09/23 수업내용 정리

### 라이브강의 정리

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
  