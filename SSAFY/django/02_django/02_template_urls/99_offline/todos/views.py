from django.shortcuts import render
from django.http.response import HttpResponse


todo_list = []

# Create your views here.
# 함수는 input에 대한 어떤 처리 후, output을 내는게 목적

# views.py에 만드는 모든 함수들의 목적은?
# 사용자의 요청(input)에 따라서 반환해야할 적절한 html(output)을 내는게 목적
def main(request):
    # main view 함수가 할 일이 늘어났다.
    # 사용자가 요청을 보냈는데... 그냥 todos/main으로 요청이 온게 아니라!
    # todos/main?work=어떤값 을 같이 담아서 보냈다.
    # 요청 할 떼 데이터도 보냈다! 그걸... 내 html에 `표현` 해줘야한다.

    # 사용자의 `모든` 요청 정보는 `request` 인자에 들어있다.
    # print(dir(request))
    print(request.GET)
    # print(request.GET['work'])
    # 여긴 파이썬인데? 그래서 그냥 나만 print 해볼 수 밖에 없는데?
    # 이걸 html에 어떻게 넘겨주지?
    # get 메서드는 찾는 key가 없으면 None을 반환한다.
    '''
        def some():
            return 
        print(some()) # None
    '''
    work = request.GET.get('work')
    if work:    # work에 값이 있을때만 (사용자가 요청헀을때만)
        todo_list.append(work)
    # print(work)
    context = {
        'todo_list': todo_list
    }
    # return HttpResponse('<h1>테스트문구</h1>')
    # app_name/templates/ 까지는 내가 안적어도 알아서 찾아간다.
    # app_name/templates/*/*.html
    # 이제 render 함수는 3번째 인자로 넘겨받은 dict에 들어있는 값들을
    # 2번째 인자로 넘겨받은 html에서 쓸 수 있게 해준다. (해석 해준다.)
    return render(request, 'todos/main.html', context)

# 생성 기능? -> 할 줄모름. 안배웠음.
# 적어도 html을 반환하는건 가능!
def create(request):



    
    return render(request, 'todos/create.html')