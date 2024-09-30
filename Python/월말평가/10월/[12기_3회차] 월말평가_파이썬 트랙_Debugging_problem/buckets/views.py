from django.shortcuts import render, redirect
from .models import TravelBucketList
from .forms import TravelBucketListForm


# Create your views here.

def index(request):
    travel_bucket_lists = TravelBucketList.objects.all()
    context = {
        'travel_bucket_lists': travel_bucket_lists
    }
    return render(request, 'buckets/index.html', context)


def about(request):
    return render(request, 'buckets/about.html')


def detail(request, bucket_pk):
    bucket_item = TravelBucketList.objects.get(pk=bucket_pk)
    context = {
        'bucket_item': bucket_item
    }
    return render(request, 'buckets/detail.html', context)


def create(request):
    if request.method == 'POST':
        # 이미지 파일도 함께 불러옴
        form = TravelBucketListForm(request.POST, request.FILES)
        if form.is_valid():
            travel_bucket_list_item = form.save()
            return redirect('buckets:detail', travel_bucket_list_item.pk)
    else:
        form = TravelBucketListForm()
    context = {
        'form': form
    }
    return render(request, 'buckets/create.html', context)


def update(request, bucket_pk):
    bucket_item = TravelBucketList.objects.get(pk=bucket_pk)
    if request.method == 'POST':
        # 각 항목 업데이트 후 저장
        # 내가 생각한 방법..
        # form = TravelBucketListForm(request.POST, request.FILES)
        # if form.is_valid():
        # # 각 항목 업데이트 후 저장
        #     # 내가 생각한 방법..
        #     bucket_item.destination_name = form['destination_name'].value()
        #     bucket_item.country = form['country'].value()
        #     bucket_item.image = form['image'].value()
        #     if form['planned_visit_date'].value():
        #         bucket_item.planned_visit_date = form['planned_visit_date'].value()
        #     if form['priority'].value():
        #         bucket_item.priority = form['priority'].value()
        #     bucket_item.save()
        #     return redirect('buckets:detail', bucket_item.pk)

        # 권고방법
        # instance 지정
        form = TravelBucketListForm(request.POST, request.FILES, instance=bucket_item)
        if form.is_valid():
            travel_bucket = form.save()
            return redirect('buckets:detail', travel_bucket.pk)
    else:
        form = TravelBucketListForm(instance=bucket_item)
    context = {
        'bucket_item': bucket_item,
        'form': form
    }
    return render(request, 'buckets/update.html', context)


def delete(request, bucket_pk):
    bucket_item = TravelBucketList.objects.get(pk=bucket_pk)
    # POST 요청인 경우
    if request.method == 'POST':
        # 버킷 리스트를 삭제하고
        bucket_item.delete()
        # 인덱스 페이지로 보냄
        return redirect('buckets:index')
    # POST 요청이 아닌경우의 return
    # 문제8번에서 의미하는 소개페이지인 bucket/bucket_pk를 detail을 통해서 보냄
    return redirect('buckets:detail', bucket_pk)
