## 07/31(화)

### 09:00 ~

- Tips
    1. `1 2 3`이 입력인 경우
        `list(map(int, input().split()))`하면 됨
    2. `123`이 입력인 경우
        `list(map(int, input()))` 하면 `A = [1, 2, 3]`이 된다.

    3. **중요**
        ```
        arr = [[0] * 3] * 2         # arr = [[0, 0, 0], [0, 0, 0]]
        print(arr)
        arr[0][0] = 1               # arr = [[1, 0, 0], [1, 0, 0]]
        print(arr)  
        ```
        과 같은 결과를 주의 해야함

        얕은 복사는 아님.    
        arr[0]과 arr[1]이 같은 대상을 참조 함


- **지그재그 순회** (숙지)

    ```
    # i행의 좌표
    # j행의 좌표

    for i in range(n):
        for j in range(m):
        function(array[i][j + (m-1-2*j)*(i%2)])
    ```
    `(m-1-2*j)*(i%2)` term의 경우, i=0,2,..에서 0이므로 0이 됨    
    `(m-1-2*j)*(i%2)` term의 경우, i=1,3,..에서 1이므로 `(m-1-2*j)`이 됨

    i가 홀수의 경우에서, 열 숫자는    
    `j + (m-1-2*j)*(i%2)`가 되므로 `m-1 - j`가 됨    
    즉, `m-1 -> m-2 -> m-3 -> ... -> 2 -> 1 -> 0`

- **델타를 이용한 2차 배열 탐색**(숙지)    
(한 좌표에서 4방향의 인접 배열 요소를 탐색하는 방법)
    1. 우측으로 = i+0 / j+1
    2. 아래방향 = i+1 / j+0
    3. 좌측으로 = i+0 / j-1
    4. 위쪽방향 = i-1 / j+0

    5. di = [0, 1, 0, -1]   
    dj = [1, 0, -1, 0]

    6. 배열이 $N \times M$인 경우   
    (수도코드)
    ```
    for i:0 -> N-1
        for j:0 -> M-1
            for k in range(4):
            ni <- i + di[k]
            nj <- j + dj[k]
            if (0 <= ni < N) and (0 <= nj < M):  # 유효한 인덱스라면
                function(array[ni][nj])
    ```

- 전치 행렬 만들기(transpose)
    ```
    for i in range(N):
        for j in range(M):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
    ```

- 역방향 대각선으로 행렬 원소 조회
    ```
    for i in range(0,N):
        function(arr[i][N-1-i])
    ```

- **파이참 디버거**연습해보기

- **부분집합 표현하기**(bit 이용)
    ```
    bit = [0]*N     # N = 집합의 크기
    for i in range(N):
        for j in range(2):
            bit[i] = j
            print(bit)
    ```

- **비트 연산자**
    1. *&* 비트 단위로 AND 연산을 한다.
    2. *|* 비트 단위로 OR 연산을 한다.

    3. **<<** 연산자

    4. **&** 연산자




