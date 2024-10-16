### 2024-10-16 Live

#### URI
- 통합 자원 식별자
- 인터넷에서 리소스(자원)을 식별하는 문자열
- 가장 일반적인 URI는 URL임
  - URL= 통합 자원 위치

#### REST API
- 일종의 guideline
- REST 규칙을 바탕으로 설계한 API = RESTful API

- 구조
  - http://www.example.com:80/path/to/myfile.html?key1=value1&key2=value2#SomewhereIntheDocument
  1. 스키마(프로토콜) ex. http
  2. 도메인 이름 ex. www.example.com
    - 직접 IP 주소를 사용하는 것이 어렵기 때문
    - 구글의 IP 주소는 142.251.42.142(이 IP 주소로 요청을 보내면 google.com으로 들어가지게 됨)
  3. 포트
    - 웹 서버의 리소스에 접근하는데 사용되는 기술적인 문
    - HTTP 프로토콜의 표준 포트
      - HTTP - 80
      - HTTPS - 443
      - 표준 포트만 작성시 생략가능
  4. Path
    - path/to/myfile.html 부분
    - 웹 서버의 리소스 경로
    - 실제 위치가 아닌(과거에는 실제위치...) 추상화된 형태의 구조를 표현

  5. Parameters
    - 웹 서버에 제공하는 추가적인 데이터
    - & 기호로 구분되는 key-value 쌍 목록
  
  6. Anchor
    - 일종의 **북마크**를 나타내며 브라우저에 해당 지점에 있는 콘텐츠를 표시
    - \# 이후 부분은 **서버에 전송되지 않음**


#### HTTP Request Methods
1. GET
  - 서버에 리소스의 표현을 요청
  - 겟을 사용하는 요청은 데이터만 검색해야함

2. POST
  - 데이터를 지정된 리소스에 제출
  - 서버의 상태를 변경

3. PUT
  - 요청한 주소의 리소스를 수정

4. DELETE
  - 지정된 리소스를 삭제

#### HTTP response status codes
- 5가지 응답 그룹으로 분류
  1. Informational responses, 1xx
  2. Successful .., 2xx
  3. ..
  4. ..
  5. ..

#### 참고
그 동안 서버가 응답했던 것 
- 지금까지 장고 서버는 사용자에게 html만 응답하고 있었음
- 하지만, 서버가 응답할 수 잇는 것은 페이지 뿐만 아니라 다양한 데이터 타입을 응답할 수 있음
- REST API는 이 중에서도 JSON 타입으로 응답하는 것을 권장

- Client $\rightarrow$ FE Framework $\rightarrow$ Django-Server
- Client $\leftarrow$ FE Framework $\leftarrow$ (JSON파일) Django-Server


### DRF with Single Model
- 장고에서 RESTful API를 쉽게 구축할 수 있도록 돕는 라이브러리

- 이를 사용하기 위해서는
  1. pip install djangorestframework
  2. settings.py에 'rest_framework'라고 등록해줘야 함
  3. project의 urls.py에 `path('api/v1/', include('libraries.urls')`를 등록해주어야 함!
#### Serialization(직렬화)
- 여러 시스템에서 활용하기 위해서 데이터 구조나 객체 상태를 나중에 재구성할 수 있는 포맷으로 변환하는 과정

- 어떠한 언어나 환경에서도 나중에 다시 쉽게 사용할 수 있는 포맷으로 변환하는 과정을 의미함

- 게시글 조회 $\rightarrow$ Serialization $\rightarrow$ Serialized data $\rightarrow$ JSON 

- **Serializer** 
  - Serialization을 진행하여 Serialized data를 반환해주는 클래스
- **ModelSerializer**
  - 장고 모델과 연결된 Serializer 클래스
  - 일반 Serializer와 달리 자동으로 모델 필드에 맞추어 Serialization을 진행

- 사용법
  1. 앱/serializers.py 파일 생성
  ```py
  from rest_framework import serializers
  from .models import Article

  class ArticleListSerializer(serializers.ModelSerializer):
      class Meta:
          model = Article
          # fields = "__all__"
          fields = ("id", "title", "content")
  ```


#### 차이/기억할 사항

- 데코레이터가 없으면 drf가 사용 할 수없음!!!!

```py
from django.urls import path
from articles import views


urlpatterns = [
    path('articles/', views.article_list),
    # path('articles/<int:article_pk>/', views.article_detail),
]
```
- 이제는 urls.py에서 app_name을 지정하지 않음
- template을 사용하지 않기 때문!

```py
# articles/views.py
from rest_framework.response import Response
# 필수임!!!
from rest_framework.decorators import api_view
from .models import Article
from .serializers import ArticleListSerializer

# 데코레이터가 없으면 drf가 사용 할 수없음!!!!1
# 어떤 요청 method에 대해서 허용할지, 작성해야함
@api_view(['GET'])
def article_list(request):
    # 전체 게시글 조회 
    # (타입: 쿼리셋, 그런데 쿼리셋은 장고에서 사용하는 데이터 타입임..)
    articles = Article.objects.all()
    # 변환하기 쉬운 포멧으로 전환(Serialization)
    # 단일 데이터면 many 무시, 다중 데이터면 many=True
    # 쿼리셋인 경우면 many 옵션 사용해야함!!!!
    serializer = ArticleListSerializer(articles, many=True)
    # 데이터만을 추출하여 제공하기 위해서 .data사용
    return Response(serializer.data)
```
이제 POSTman or browser를 통해서 요청 확인해보자!


- 과거 view 함수와의 응답 데이터 비교(같은 데이터)
  - 과거: HTML에 출력되도록 페이지와 함께 응답하는 view함수!
  - 현재: JSON 데이터로 serialization하여 페이지 없이 응답하는 view함수!



- 새로운 시리얼라이저를 만들어서 진행했음.. 왜???
- 거기서는 fields가 그냥 달라서 새로 만들어 준것!
- 쉽게 말해, 다른 종류의 가공기구를 만들어 두고 사용한 것.
- 따라서 ,필요에 따라 만들고 사용하면 됨!
```py
#articles/serializers.py
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"
# ========================================

#articles/urls.py

from django.urls import path
from articles import views


urlpatterns = [
#    path('articles/', views.article_list),
    path('articles/<int:article_pk>/', views.article_detail),
]
# ========================================

#articles/views.py
from rest_framework.response import Response
# 필수임!!!
from rest_framework.decorators import api_view
from .models import Article
from .serializers import ArticleListSerializer
from .serializers import ArticleSerializer
@api_view(['GET'])
def article_detail(request, article_pk):
    # 단일 게시글 조회
    article = Article.objects.get(pk=article_pk)
    # 시리얼라이즈
    serializers = ArticleSerializer(article)
    return Response(serializers.data)
```

- POST 요청 관련 코드
```py
# 데코레이터가 없으면 drf가 사용 할 수없음
# 어떤 요청 method에 대해서 허용할지, 작성해야함
# @api_view()이면, GET만 허용
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        # 전체 게시글 조회 
        # (타입: 쿼리셋, 그런데 쿼리셋은 장고에서 사용하는 데이터 타입임..)
        articles = Article.objects.all()
        # 변환하기 쉬운 포멧으로 전환(Serialization)
        # 단일 데이터면 many 무시, 다중 데이터면 many=True
        serializer = ArticleListSerializer(articles, many=True)
        # 데이터만을 제공하기위해서
        return Response(serializer.data)
    
    # drf에서는 elif를 사용해서 명확하게 조건을 명시하는 것을 권장함!!!!!!!!
    # else말고!
    elif request.method == 'POST':
        # 모델시리얼라이저를 사용해서 사용자 입력 데이터를 받아 
        # 직렬화를 진행하기 위함
        serializer = ArticleSerializer(data=request.data)
        # 유효성 검사
        # drf 개발자들이 같은 이름으로 유효성 검사 메서드 만들어 놓음
        if serializer.is_valid():
            serializer.save()
            # 저장 성공 후, 201 응답 상태코드를 반환해야 함 
            # status로 상태코드를 보냄 안쓰면 200임!!!
            # 우리는 201을 보내기 위해 입력
            # from rest_framework import status 필요함
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # 유효성 검사 실패 후 400 응답 상태코드를 반환해야 함
        # 에러도 같이 반환해줌!!
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

- 게시글 데이터 삭제하기!
  - 요청에 대한 데이터 삭제가 성공시 204 No Content응답!

```py
@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    # 단일 게시글 조회
    article = Article.objects.get(pk=article_pk)
    
    if request.method == 'GET':
        # 시리얼라이즈
        serializers = ArticleSerializer(article)
        return Response(serializers.data)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    # 데이터 수정위함
    elif request.method == 'PUT':
        # 내용의 일부만 업데이트 하기 위함!! 부분수정
         serializer = ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

Tips!
```py
# raise_exception=True 사용시 마지막의 400 BAD_REQUEST return 안써도됨!!
if serializer.is_valid(raise_exception=True):
  pass
# return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```