## 08/01(목)

### 09:00 ~
- 검색
    1. 순차검색(sequential search)
        (1) 정렬이 안된 경우
        (2) 정렬이 된 경우

        - 배열을 검사하고 인덱스에 접근하는 경우에는    
        항상 인덱스 검사를 먼저 해야함!!
            ```
            while i<n and a[i] < key:
            ```
            왜? 단축평가!! + **a[i]먼저 검사하면 에러남!**
            ```
            while a[i] < key and i < n
            ```

    2. 이진검색(binary search)
        - 자료가 정렬된 상태여야 함!
        - 자료의 삽입/삭제가 배열을 항상 정렬로 유지하는 추가 작업이 필요.

        - 라이브에서는 퀵 소트 패스한듯..
    3. 해쉬(hash)

- 선택정렬

    ```
    def selection_sort(arr, N):
        for i in range(N-1):
            min_idx = i
            for j in range(i+1, N):
                if arr[min_idx] > arr[j]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i] # 구간의 최솟값을 기준위치로 이동

        return arr

    A = [2, 7, 5, 3, 4]
    B = [4, 3, 2, 1]
    print(selection_sort(A, len(A)))
    print(selection_sort(B, len(B)))
    ```
    
    **선택정렬의 장단점** 기억 

***
***
**GitHud - 잔디 관리좀 해야함..**
***
***