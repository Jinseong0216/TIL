##

### 09:00 ~
- 버블 정렬: 코드 단순, 알고리즘 단순, 시간이 오래걸림

- 카운팅 정렬: 연산량 적음, 코드가 상대적으로 복잡, n이 작아야 가능
    1. 보통 배열의 길이가 100만 이하의 정수면 할만함
    2. 정수나 정수로 표현 할 수 있는 자료에 대해서 적용 가능
    3. computational complexity = $ O(n + k) $, where $ n = len(arr) \& |arr| < k $.
    ```
    arr = list(map(int, input().split()))
    counts = [0] * (k+1)                    
    temp = [0] * n                          

    for i in range(len(arr)):
        counts[arr[i]] += 1                 # n번

    for i in range(1, k+1):
        counts[i] += counts[i-1]            # k번 

    for i in range(len(arr)-1, -1, -1):
        counts[temp[i]] -= 1                # n번 (파이썬 식 인덱스로 인함.)
        temp[counts[arr[i]]] = arr[i]       # n번
    ```
    - `temp[counts[arr[i]]] = arr[i]`는 뒤에서 부터 채우는 것임    
        ex. arr = [4,0,1,1,1,2,2,2] -> counts = [1,4,7,8] -> temp = [0,1,1,1,2,2,2,4]
        
        ㅁㅁㅁㅁㅁㅁㅁㅁ $ \rightarrow $ ㅁㅁㅁㅁㅁㅁ2ㅁ $ \rightarrow $ ㅁㅁㅁㅁㅁ22ㅁ $ \rightarrow $ ㅁㅁㅁㅁ222ㅁ $ \rightarrow $ ㅁㅁㅁ1222ㅁ $ \rightarrow $ ㅁㅁㅁ1222ㅁ $ \rightarrow $ ㅁ111222ㅁ $ \rightarrow $ 
        0111222 $ \rightarrow $ 01112224

    -  위의 과정을 보면 3n + k번 정도 연산함을 알 수 있음

- 그리디 알고리즘
    1. 해 선택
    2. 실행 가능성 검사
    3. 해 검사


- Tips
    아주 유용함.
    ```
    num = 456789
    c = [0] * 12

    for i in range(6):
        c[num % 10] += 1
        num //= 10

    >>> num = [0,0,0,0,1,1,1,1,1,1,0,0]
    ```

    ```
    import sys
    sys.stdin = open('input.txt')
    numbers = list(map(int, input().split()))
    ```
    한다면(같은 디렉토리에 input.txt 있어야함) 자동으로 한 줄을 불러옴!!