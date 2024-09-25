## 09/25

### 유효성 검사 via Django Form
Django가 제공하는 form을 통해서 검사하면 편함.

- Django Form: 사용자 입력 데이터를 수집하고 처리 및 유효성 검사를 수행하기 위한 도구
forms.py로 보통 만듬

model에서의 필드와 form에서의 필드가 다른이유는??
  - form에서는 TextField가 존재하지 않음
  - form Field와 model Field는 다름

- views.py에서는 `from .forms import 폼클래스 이름`으로 불러옴

```
  <form action="{% url "articles:create" %}" method="POST">
    {% csrf_token %}
    {{ form }}
    {% comment %} <div>
      <label for="title">Title: </label>
      <input type="text" name="title" id="title">
    </div>
    <div>
      <label for="content">Content: </label>
      <textarea name="content" id="content"></textarea>
    </div> {% endcomment %}
    <input type="submit">
```
을
```
  <form action="{% url "articles:create" %}" method="POST">
    {% csrf_token %}
    {{ form }}
    <input type="submit">
  </form>
```
으로 바꿀 수 있음

### Form rendering option
form.as_p와 같이 4가지 옵션이 제공이 됨
as_p: 일반적으로 사용
as_div
as_table
as_p
as_ul

### Widget 적용
- 공식문서를 통해 built-in 위젯을 사용하는 것 추천

### 장고에서의 폼 종류는 2가지
- Form
  - 사용자 입력 데이터를 DB에 저장하지 않을 때.(검색, 로그인)

- ModelForm
  - 사용자 입력 데이터를 DB에 저장해야 할 때.(게시글 작성, 회원가입)

- **ModelForm**
  - 기존 ArticleForm 클래스 수정
  - 모델을 상속해오기(클래스를)
  - Form클래스 안에
    - 
        ```py
        class Meta:
            model = Article
            fields = '__all__'
        ```
        를 추가해 줌(fields 변수명을 바꾸면 안됨!! )

    차이
    ```py
    from django import forms 
    # 모델폼을 위한 모델 불러오기
    from .models import Article

    # 폼
    class ArticleForm(forms.Form):
        title = forms.CharField(max_length=10)
        contnet = forms.CharField(widget=forms.Textarea)

    # 모델 폼
    class ArticleForm(forms.ModelForm):
        class Meta:
            model = Article
            fields = '__all__'
    ```

    - 즉, 귀찮게 모델의 정보를 하나하나 입력할 필요 없어짐
  
    - **Meta class**
      - `exclude = ('필드명',)`을 넣고
      - `fields = '__all__'`을 주석처리하여 특정 속성 없이 사용 가능


- 모델폼 인스턴스 생성(사용자 입력 데이터를 통째로 인자로 작성)
```py
def create(request):
#     title = request.POST.get('title')
#     content = request.POST.get('content')
    # 1. 모델폼 인스턴스 생성(사용자 입력 데이터를 통째로 인자로 작성)
    form = ArticleForm(request.Post)

    # 2. 유효성 검사
    if form.is_valid():
        # 3. 저장
        article = form.save()        
        return redirect('articles:detail', article.pk)
    # 유효성 검사 실패시
    context = {
        'form': form,
    }
    # 에러 메세지를 원래 페이지에 주기 위해서
    # 장고는 알아서 실패 이유를 넘겨줌!
    return render(request, 'articles/new.html', form)
```


### is_valid()
- 공백데이터가 유효하지 않은 이유
    - 별도로 명시하진 않아도 모델 필드에는 기본적으로 빈 값 허용 x인 제약 있음


### 나머지, edit, update등 비슷하게 사용가능.

#### new vs craete in view
- 공통점: 데이터 생성을 구현하기 위함
- 차이점: new는 GET method 요청만을, create는 POST method 요청만을 처림
- **HTTP request method**차이점을 활용해 두 함수를 하나로 구조화 가능

이전
```py
def new(request):
    form = ArticleForm()
    context = {
        'form': form,
    }
    # 게시글 작성 페이지 응답
    return render(request, 'articles/new.html', context)


def create(request):
#     title = request.POST.get('title')
#     content = request.POST.get('content')
    # 1. 모델폼 인스턴스 생성(사용자 입력 데이터를 통째로 인자로 작성)
    form = ArticleForm(request.POST)

    # 2. 유효성 검사
    if form.is_valid():
        # 3. 저장
        article = form.save()
        return redirect('articles:detail', article.pk)
    # 유효성 검사 실패시
    context = {
        'form': form,
    }
    # 에러 메세지를 원래 페이지에 주기 위해서
    # 장고는 알아서 실패 이유를 넘겨줌!
    return render(request, 'articles/new.html', context)
```

개선
```py
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)
```

#### edit과 update 합치기
이전
```py
def edit(request, pk):
    # 어떤 게시글을 수정할지 조회
    article = Article.objects.get(pk=pk)
    
    # 추가
    form = ArticleForm(instance=article)

    context = {
        'article': article,
        # 추가
        'form': form
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    # 1. 어떤 게시글 수정할지 조회
    article = Article.objects.get(pk=pk)
    # 2. 사용자로부터 받은 새로운 입력 데이터 추출
    form = ArticleForm(request.POST, instance=article)
    if form.is_valid():
        form.save()
        return redirect('articles:detail', article.pk)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/edit.html', context)
```

개선
```py
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detial', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    render(request, 'articles/update.html', context)
```