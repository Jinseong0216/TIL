from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
import pandas as pd
import random
from queue import PriorityQueue
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64

# ==================================================
# 전역변수로 DataFrame 미리 설정하기
df = pd.read_csv('./data/test_data.CSV', encoding='cp949')
df_has_null = pd.read_csv('./data/test_data_has_null.CSV', encoding='cp949')
df.columns = df_has_null.columns = ['name', 'age', 'sex', 'job', 'residential_area']

# READEM.md 보여주기
def index(request):
    # 테스트 데이터를 기반으로 한 분석 그래프 생성
    graph = generate_graph()
    return render(request, 'index.html', {'graph': graph})

# ==================================================
# 그래프 생성 함수
def generate_graph():
    # Locust 테스트 데이터를 기반으로 한 분석 예시
    # 임시 데이터 (실제 Locust 결과 데이터로 대체할 수 있습니다)
    data = {
        'endpoint': [
            '/test/bubble_sort/', '/test/mean_age/', '/test/my_data/', 
            '/test/my_data_has_null/', '/test/normal_sort/', '/test/priority_queue/'
        ],
        'requests': [515, 479, 506, 527, 485, 549],
        'failures': [0, 0, 0, 0, 0, 0],
        'average_response_time': [40, 11, 8, 9, 9, 10],
    }

    # Pandas DataFrame으로 변환
    df_stats = pd.DataFrame(data)

    # Seaborn으로 그래프 생성
    plt.figure(figsize=(10, 6))
    sns.set(style="whitegrid")

    # 요청 수와 평균 응답 시간에 대한 그래프
    fig, ax1 = plt.subplots(figsize=(10, 6))

    ax1.bar(df_stats['endpoint'], df_stats['requests'], color='skyblue', label='Requests')
    ax1.set_xlabel('Endpoint')
    ax1.set_ylabel('Requests', color='skyblue')
    ax1.tick_params(axis='y', labelcolor='skyblue')

    ax2 = ax1.twinx()
    ax2.plot(df_stats['endpoint'], df_stats['average_response_time'], color='red', marker='o', label='Avg Response Time')
    ax2.set_ylabel('Average Response Time (ms)', color='red')
    ax2.tick_params(axis='y', labelcolor='red')

    plt.title('Locust Test Analysis: Requests and Average Response Time')
    fig.tight_layout()

    # 그래프를 이미지로 변환하여 base64로 인코딩
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    graph_image = base64.b64encode(buffer.read()).decode('utf-8')
    buffer.close()

    return graph_image

# ==================================================
# 관통 과제A에 해당하는 함수: CSV 데이터를 DataFrame으로 변환 후 반환
def my_data(request):
    data = df.to_dict('records') 
    return JsonResponse({'data': data})

# 관통 과제B에 해당하는 함수: CSV 데이터의 결측치 전처리
def my_data_has_null(request):
    df_has_null.fillna('NULL', inplace=True)
    data_has_null = df_has_null.to_dict('records')
    return JsonResponse({'data_has_null': data_has_null})

# 관통 과제C에 해당하는 함수: 평균 나이와 가장 비슷한 나이인 10개 행을 새로운 DataFrame으로 만들어 반환
def mean_age(request):
    mean_age = round(df_has_null[['age']].mean(numeric_only=True), 2)
    df_has_null['age_diff'] = (df_has_null['age'] - mean_age).abs()
    top_10_diff = df_has_null.sort_values(by='age_diff').head(10)
    data = top_10_diff[['name', 'age', 'sex', 'job', 'residential_area']].to_dict('records')
    return JsonResponse({'data': data})

# ==================================================
# 버블정렬
@api_view(['GET'])
def bubble_sort(request):
    li = [random.choice(range(1, 5000)) for _ in range(1000)]
    for i in range(len(li) - 1, 0, -1):
        for j in range(i):
            if li[j] < li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
    context = {'top': li[0]}
    return JsonResponse(context)

# 내장 메서드 sort()
@api_view(['GET'])
def normal_sort(request):
    li = [random.choice(range(1, 5000)) for _ in range(1000)]
    li.sort(reverse=True)
    context = {'top': li[0]}
    return JsonResponse(context)

# 우선순위 큐
@api_view(['GET'])
def priority_queue(request):
    pq = PriorityQueue()
    for i in range(1000):
        pq.put(-random.choice(range(1, 5000)))
    context = {'top': -pq.get()}
    return JsonResponse(context)

# ==================================================
