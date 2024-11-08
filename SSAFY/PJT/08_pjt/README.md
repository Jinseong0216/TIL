# 프로젝트: Django 기반 API 성능 분석 및 개선(최진성)

## 1. 프로젝트 개요

이 프로젝트는 Django 웹 애플리케이션을 사용하여 성능 분석 및 개선 작업을 다루고 있습니다. Locust를 사용한 성능 테스트 결과를 시각화하고, 다양한 알고리즘의 성능을 비교합니다. 또한, 데이터를 CSV 파일에서 로드하고, API 엔드포인트를 통해 데이터를 제공하거나, 알고리즘을 실행하는 다양한 기능을 구현합니다.

---

## 2. 기능 및 URL별 설명

### 1) **`/` (index)**
- **기능**: `README.md` 파일을 보여주는 메인 페이지입니다. 이 페이지에서는 테스트 데이터를 기반으로 한 성능 분석 그래프가 표시됩니다. 이를 통해 Locust 테스트의 결과를 시각적으로 확인할 수 있습니다.
- **주요 코드**:
    ```python
    def index(request):
        graph = generate_graph()
        return render(request, 'index.html', {'graph': graph})
    ```
    이 코드에서는 `generate_graph()` 함수를 호출하여 Locust 테스트 결과를 시각화한 그래프를 생성하고, 이를 `index.html` 템플릿에 전달합니다.

### 2) **`/my_data/`**
- **기능**: CSV 파일을 `pandas` DataFrame으로 변환하여, 이를 JSON 형태로 반환합니다. 데이터를 사용하여 다양한 분석을 할 수 있습니다.
- **주요 코드**:
    ```python
    def my_data(request):
        data = df.to_dict('records')
        return JsonResponse({'data': data})
    ```
    `df.to_dict('records')`는 CSV 데이터를 리스트 형태로 변환하여, 클라이언트에게 JSON 형식으로 반환합니다.

### 3) **`/my_data_has_null/`**
- **기능**: 결측치가 포함된 CSV 데이터를 전처리하여 `NULL` 값으로 채운 후 반환합니다.
- **주요 코드**:
    ```python
    def my_data_has_null(request):
        df_has_null.fillna('NULL', inplace=True)
        data_has_null = df_has_null.to_dict('records')
        return JsonResponse({'data_has_null': data_has_null})
    ```
    `df_has_null.fillna('NULL', inplace=True)`는 결측치가 있는 데이터를 `NULL`로 채웁니다. 이를 처리한 후 JSON 형태로 반환합니다.

### 4) **`/mean_age/`**
- **기능**: 평균 나이와 가장 비슷한 나이를 가진 10개의 데이터를 반환합니다.
- **주요 코드**:
    ```python
    def mean_age(request):
        mean_age = round(df_has_null[['age']].mean(numeric_only=True), 2)
        df_has_null['age_diff'] = (df_has_null['age'] - mean_age).abs()
        top_10_diff = df_has_null.sort_values(by='age_diff').head(10)
        data = top_10_diff[['name', 'age', 'sex', 'job', 'residential_area']].to_dict('records')
        return JsonResponse({'data': data})
    ```
    이 코드는 `age` 컬럼의 평균을 구하고, 각 나이와 평균 나이의 차이를 계산한 후 가장 비슷한 10개의 데이터를 추출하여 반환합니다.

### 5) **`/normal_sort/`**
- **기능**: Python 내장 정렬 메서드(`sort()`)를 사용하여 랜덤으로 생성된 1000개의 수를 내림차순으로 정렬하고, 가장 큰 값을 반환합니다.
- **주요 코드**:
    ```python
    def normal_sort(request):
        li = [random.choice(range(1, 5000)) for _ in range(1000)]
        li.sort(reverse=True)
        context = {'top': li[0]}
        return JsonResponse(context)
    ```
    `li.sort(reverse=True)`를 사용하여 리스트를 내림차순으로 정렬하고, 정렬된 리스트에서 가장 큰 값인 `li[0]`을 반환합니다.

### 6) **`/priority_queue/`**
- **기능**: 우선순위 큐(Priority Queue)를 사용하여 1000개의 랜덤 수를 저장하고, 가장 큰 값을 반환합니다.
- **주요 코드**:
    ```python
    def priority_queue(request):
        pq = PriorityQueue()
        for i in range(1000):
            pq.put(-random.choice(range(1, 5000)))  # 음수로 넣어서 큰 값이 우선되도록
        context = {'top': -pq.get()}
        return JsonResponse(context)
    ```
    우선순위 큐에 값을 음수로 넣어서 최대값이 먼저 나오도록 하고, `pq.get()`으로 우선순위가 높은 값을 반환합니다.

### 7) **`/bubble_sort/`**
- **기능**: 버블 정렬을 사용하여 1000개의 랜덤 수를 정렬하고, 가장 큰 값을 반환합니다.
- **주요 코드**:
    ```python
    def bubble_sort(request):
        li = [random.choice(range(1, 5000)) for _ in range(1000)]
        for i in range(len(li) - 1, 0, -1):
            for j in range(i):
                if li[j] < li[j + 1]:
                    li[j], li[j + 1] = li[j + 1], li[j]
        context = {'top': li[0]}
        return JsonResponse(context)
    ```
    버블 정렬을 구현하여 가장 큰 값이 정렬된 리스트의 첫 번째로 오도록 합니다. 이 알고리즘은 O(n²)의 시간 복잡도를 가집니다.

---

## 3. 기타 주목할 만한 코드

### 1) **그래프 생성 (`generate_graph` 함수)**
- **기능**: Locust 성능 테스트 결과를 시각화하는 그래프를 생성합니다. 이 그래프는 각 엔드포인트에 대한 요청 수와 평균 응답 시간을 보여줍니다.
- **주요 코드**:
    ```python
    def generate_graph():
        data = {
            'endpoint': ['/test/bubble_sort/', '/test/mean_age/', '/test/my_data/', 
                         '/test/my_data_has_null/', '/test/normal_sort/', '/test/priority_queue/'],
            'requests': [515, 479, 506, 527, 485, 549],
            'failures': [0, 0, 0, 0, 0, 0],
            'average_response_time': [40, 11, 8, 9, 9, 10],
        }
        df_stats = pd.DataFrame(data)
        plt.figure(figsize=(10, 6))
        sns.set(style="whitegrid")
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

        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        graph_image = base64.b64encode(buffer.read()).decode('utf-8')
        buffer.close()

        return graph_image
    ```

    이 함수는 `matplotlib`과 `seaborn`을 이용해 요청 수와 평균 응답 시간을 비교하는 그래프를 생성합니다. 그래프는 base64로 인코딩되어 클라이언트로 전달됩니다.
    (해당 시각화는.. 예쁘게 만드는게 어려워서 GPT 이용함; 그나마 볼만하게 만드는건 어렵더라...)
---

## 4. 어려웠던 점

### 1) **Locust 테스트 데이터 시각화**
Locust에서 생성된 성능 테스트 데이터를 시각화하는 작업이 다소 복잡했습니다. 특히, `matplotlib`과 `seaborn`을 사용해 응답 시간과 요청 수를 동시에 비교하는 그래프를 만드는 부분이 어려웠습니다. 이를 해결하기 위해 `twinx()`를 사용하여 두 가지 축을 공유하는 그래프를 만들었습니다.

### 2) **Pandas DataFrame 경로 찾기...**
경로를 잘못 알고있어서 나중에 수정하려고 하니 좀 시간이 걸림.

---

## 5. 결론

이번 프로젝트에서는 Django를 이용해 다양한 성능 테스트와 데이터 처리 기능을 제공하며, Locust를 통해 실시간 성능 분석을 시각화할 수 있었습니다. 성능 최적화와 데이터 처리, 그리고 알고리즘 분석을 통해 웹 애플리케이션의 효율성을 높이는 방법을 배웠습니다.
