## 09/26 강의내용 정리

### Static Files
- 정적 파일
- 서버 측에서 변경되지 않고 고정적으로 제공되는 파일일
- 이미지, JS, CSS파일 등

- **스태틱 파일 기본 경로**
    - app폴더/static/

#### 웹 서버와 정적 파일
- 웹 서버 기본 동작은`
- 특정 위치에 있는 자원을 요청(HTTP request) 받아서
- 응답(HTTP response)를 처리하고 제공하는 것

Client $\rightarrow$ HTTP request $\rightarrow$ Server $\rightarrow$ HTTP response

#### 태그를 통한 스태틱 파일 사용
- 스태틱 파일의 경로는 DTL의 스태틱 태그를 사용해야 함
- 빌트인 태그가 아니기 때문에 load tag를 사용해 import 후 사용 가능

- {% load static %}를 html**제일 위**에 
- 바디
  - `<img src="{% static "articles/sample-1.png" %}" alt="sample-image">`

- base.html에서 load static을 한다면 자식 템플릿에서도 가능한가?
  - **적용이 안됨**

#### STATIC_URL
- 기본경로
    - settings.py에서 `STATIC_URL = 'static'/` 해줘야함
    - 실제 물리적인 주소가 아니므로 바꿔도 상관은 없음.
    - URL + STATIC_URL + 정적파일 경로

- 추가경로
  - settings.py에서 STATICFILES_DIRS = [추가경로] 해줘야함
  ```py
  STATICFILES_DIRS = [
    BASE_DIR / 'static',
  ]
  ```   
  - STATICFIELD_DIRS에 문자열 값으로 추가 경로 설정
  - STATICFIELD_DIRS
    - 정적 파일의 기본경로 외에 추가적인 경로 목록을 정의하는 리스트

### Media Files
- 정적파일의 일부로서 
- 서버가 미리배치 X
- 사용자가 업로드한 파일을 의미함
- user-uploaded files

#### ImageField()
- 이미지 업로드에 사용하는 모델 필드
- 이미지 객체가 직접 DB에 저장되는 것이 아니라
    - **이미지 파일의 경로** 문자열이 저장됨
    - 이미지필드이지만, 실제로는 문자열필드의 일부로서 기능하는 듯
    - default로 100자 최대길이로 되어있음

- **미디어 파일을 제공하기 전 준비사항**
    - pip install pillow필요함
    - 장고 공식문서를 보면서 하면 됨
    1. settings.py에 MEDIA_ROOT, MEDIA_URL설정
    ```py
    MEDIA_ROOT = BASE_DIR / 'media'
    MEDIA_URL = 'media/'
    ```
    2. 작성 MEDIA_ROOT와 MEDIA_URL에 대한 URL 지정
    ```py
    # 프로젝트의 urls.py임
    from django.contrib import admin
    from django.urls import path, include
    # 새 모듈 추가
    from django.conf import settings
    # 새 모듈 추가
    from django.conf.urls.static import static

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('articles/', include('articles.urls')),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # 스태틱 주소, 미디어파일의 실제 위치
    ```

    이미 테이블이 만들어 진 경우, 이미지를 추가 하면 항상 마지막에 붙음!
    
    3. 마이그레이션 진행(필요에 의해)


    - 현재 상테에서 이미지 업로드를해도 테이블에 추가되지 않음.. 왜?
        - form의 문제임 디폴트로 text만 받게 되어있으므로
         
    4. enctype을 지정해줘야 함
       - `  <form action="{% url "articles:create" %}" method="POST" enctype="multipart/form-data">`
       
       그러나 아직 더 셋팅 해야함
       파일은 기본적으로 url을 통해서 전달되지 않으므로 
       -  create함수안에서 `form = ArticleForm(request.POST, request.FILES)`을 해줘야함
    
    - **여기까지 해줘야 이미지의 경로를 나의 테이블에 추가 한 것!**

    - 그러나 **업로드 이미지 제공하기**도 해야함
    
    1. `<img src="{{ articles.image.url }}" alt="img">` 와 같은 느낌으로 하면 사용 가능!!
       - 같은 이름인경우는 어떻게? 
       - 알아서 해결됨.(그래서 MEDIA_URL)을 setting에 사용한듯?
       - 같은 이름으로 업로드하면 장고가 알아서 다른 구별자를 줌
    
    2. 이미지가 있는 경우에만 출력하도록 변경
    ```
    {% if article.image %}
    <img src="{{ articles.image.url }}" alt="img">
    {% endif %}
    ```

    - **이미지의 수정**은 어떻게?
    1. 업데이트쪽에
        - `<form action="{% url "articles:update" article.pk %}" method="POST" enctype="multipart/form-data">`
    2. 뷰 함수 수정(업데이트)
        - `form = ArticleForm(request.POST, request.FILES, instance=article)`

#### 미디어파일 추가 경로
- uploaed_to 
```py
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()

    # 이미지 필드 추가
    # 당연히 모든 모델필드는 공백 허용X
    # 즉, 이대로 만들면 모든 사용자는 항상 글을 업로드 해야만하게 됨
    # 따라서 빈 값을 허용하도록 셋팅해야함!!! blank=True
    # image = models.ImageField(bland=True)

    #1. 기본 경로 설정
    # 기본경로/images/ 안에 파일이 업로드가 됨
    # image = models.ImageField(bland=True, uploaed_to='images'/)

    #2. 업로드 날짜로 경로 설정
    # 기본경로/images/ 안에 파일이 업로드가 됨
    # image = models.ImageField(bland=True, uploaed_to='%Y/%m/%d/')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

```
