from django.shortcuts import render
from django.http.response import HttpResponse


todo_list = []

# Create your views here.
def main(request):
    work = request.GET.get('work')
    if work:
        todo_list.append(work)
    context = {
        'todo_list': todo_list
    }
    return render(request, 'todos/main.html', context)


def create(request):
    return render(request, 'todos/create.html')