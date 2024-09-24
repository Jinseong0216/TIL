from django.shortcuts import render, redirect
# 모델 클래스 가져오기
from .models import Article


# Create your views here.
def index(request):
    # 게시글 전체 조회 요청 to DB
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


# 항상 request먼저 받음
def detail(request, pk):
    # url로부터 전달받은 pk를 활용해 데이터를 조회 
    # get의 경우, 데이터가 2개이상 or 없으면 예외발생함
    # 왼쪽의 pk는 article 모델의 field(attribute. 속성.)임
    # 오른쪽의 pk는 함수의 인자로 받은 것
    # 사실 id=pk로 해도 되긴함(권장 X)
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


def new(request):
    # 게시글 작성 페이지 응답
    return render(request, 'articles/new.html')

# 과거 catch와 같은 역할
def create(request):
    # 1. 사용자 요청으로부터 입력 데이터를 추출
    # title = request.GET.get('title')
    # content = request.GET.get('content')
    title = request.POST.get('title')
    content = request.POST.get('content')


    # 2. 추출한 입력 데이터를 활용해 DB에 저장 요청
    # 저장하기 (데이터의 유효성 검사로 인해 3번 사용X) (1번은 비효율적이라 사용X) 보통...
    # 저장 1
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 저장 2
    article = Article(title=title, content=content)
    article.save()

    # 저장 3
    # Article.objects.create(title=title, content=content)

    # return render(request, 'articles/create.html')
    # 실제로는 렌더링 보다는 다시 클라이언트가 요청을 보내게 하기 때문에 아래의 방식이 옳음
    # 
    return redirect('articles:detail', article.pk)
        

def delete(request, pk):
    # 어떤 게시글을 삭제할지 조회
    article = Article.objects.get(pk=pk)
    # 조회한 게시글 삭제
    article.delete()
    return redirect('articles:index')


def edit(request, pk):
    # 어떤 게시글을 수정할 지 조회
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/edit.html', context)


def update(request, pk):
    # 어떤 게시글을 수정할 지 조회
    article = Article.objects.get(pk=pk)
    # 사용자로부터 받은 새로운 입력 데이터 추출
    title = request.POST.get('title')
    content = request.POST.get('content')
    # 기존 게시글의 데이터를 사용자로 받은 데이터로 새로 할당
    article.title =title
    article.content = content
    # 저장
    article.save()

    return redirect('articles:detail', article.pk)