from django.shortcuts import render
# 모델 클래스 가져오기
from .models import Garage

# Create your views here.
def index(request):
    # 게시글 전체 조회 요청 to DB
    garages = Garage.objects.all()
    context = {
        'garages': garages,
        'result_1': garages.get(location='독도'),
        'result_2': garages.filter(capacity__lte=30),        
        'result_3': garages.filter(is_parking_avaliable=True),        
    }
    return render(request, 'garages/index.html', context)