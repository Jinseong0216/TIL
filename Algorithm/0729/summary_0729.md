## 07/29(월)

### 14:00 ~

- 좋은 알고리즘이란?
    1. 정확성
    2. 작업량
    3. 메모리 사용량
    4. 단순성
    5. 최적성(최적화)

- Tips.
    1. 데이터가 많으면 append를 잘 안쓰는 것이 좋음(느려짐)
    2. split(' ') 하지 않기(공백 한 칸이 아니라 두 칸 혹은 세 칸이 주어질 수도 있음..)
    3. 아래의 코드에서 if조건문의 형식과 아래의 순서를 맞추는 것이 보기 좋음
        - ex. max_value < arr[i]와 max_value = arr[i]
    4. 아래의 코드에서 간혹 이미 계산한 결과를 다시 계산하는 사람이 있음. 그러지 말기
        - ex. `for i in range(1, len(arr))`이런 식으로 쓰지 않기

```
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_value = arr[0]
    for i in range(1, N):
    if max_value < arr[i]:
        max_value = arr[i]
```

- 버블 정렬: 시간 복잡도 $ O(n^2) $
    
    1. $ n + (n-1) + (n-2) + ... + 2 + 1 = \frac{n(n+1)}{2} = \frac{1}{2} \cdot n^2 + \frac{1}{2} \cdot n$ 이므로 $ O(f) = O(n^2) $
    
    2. 구간의 끝은 2개 남은 경우를 의미함!

    3. `arr[j], arr[j+1] = arr[j+1], arr[j]` 이런 식으로 해도 잘 되는 이유는 뭘까..?
        오른쪽에서 왼쪽으로 코드가 진행되기 때문..?

    4. 버블 **정렬**이란 의미에서는 내가 생각한 방향보다 라이브 강의에서 제시한 방향이 맞는듯?!!
    
    내 생각
    ```
    seq = list(map(int, input().split()))
    N = len(seq)

    for i in range(N):
        for j in range(i, N-1):
            x, y = seq[j], seq[j+1]
            if x > y:
                seq[j], seq[j+1] = y, x
    print(seq)
    ```

    라이브 강의
    ```
    N = 6
    arr = [7, 2, 5, 3, 4, 1]

    for i in range(N-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    print(arr)
    ```

1. **Solving Club에서 SWEA HW은 필수!!!**

2. **발표 위주의 수업 예정(내가 푼 문제)**

3. **11:00 ~ 13:00 개인 학습**

4. **13:00 ~ 15:00 그룹 학습**

5. **그룹 중 한명이 나와서 발표**


- solving club에 있는 문제 다풀어 보자!!!