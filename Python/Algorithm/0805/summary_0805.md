## 08/05(월)
- A형 대비
- 강사님 데이터 트랙 강의 중 (DFS/BFS)까지만 보기
- 실제 난이도가 강사님 올려준 문제 중 5번(보호필름)정도 예상.

### 금일 알고리즘 실습 문제

실습 순서 : 복습 문제 => 연습 문제 => 필수 과제 => 실습 문제

실습문제(4861) 위치: SWEA -> LEARN -> Course -> Programming Intermediate -> String ( [링크](https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVGOEKqeoDFAWg) )
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   필수 과제 : 회문2 (1216)
*   복습 문제 :
    *   (1) Ladder1(1210)
    *   (2) Ladder2(1211) → (어려울수 있으니, 어려우면 제일 마지막에 풀어보기, 하루종일 이 문제만 잡아놓기 XXXXX)
*   연습 문제 :
    *   (1) string (1213) → bruteforce(고지식한 방식)으로 풀어보기
*   실습 문제 :
    *   (1) 회문 (4861)
    *   (2) 가장 빠른 문자열 타이핑(3143)


- 패턴매칭
```
i = j = 0
while i < N and j > M:
    if t[i] = t[j]:
        i += 1
        j += 1
    else:
        i = i-j+1
        j = 0
```

회문2
```
def pal_len(grid):
    for k in range(100,0,-1):
        for i in range(200):
            for j in range(100 - k + 1):
                if grid[i][j:j + k] == grid[i][j:j + k][::-1]:
                    return k

for t in range(1, 2):
    dummy_input = input()
    grid1 = [input().strip() for _ in range(100)]
    grid2 = [''.join(grid1[j][i] for j in range(100)) for i in range(100)]
    grid = grid1 + grid2

    ans = pal_len(grid)
    print(f'#{t} {ans}')


    M = 0
    k = M + 1
    for i in range(200):
        while k < M + 3:
            for j in range(100-k+1):
                if grid[i][j:j+k] == grid[i][j:j+k][::-1]:
                    M = k
                    break
            k += 1
        k = M + 1
    ans = M
    print(f'#{t} {ans}')
```

두 코드의 차이를 모르겠음.


- 문자열 매칭
```
for _ in range(10):
    tc = int(input())
    pattern = input()
    search_text = input()
    result = 0

    compare_idx = 0
    pattern_idx = 0

    while compare_idx < len(search_text):
        if search_text[compare_idx] != pattern[pattern_idx]:
            compare_idx = compare_idx - pattern_idx + 1
            pattern_idx = 0
            continue

        pattern_idx += 1
        compare_idx += 1

        if pattern_idx == len(pattern):
            result += 1
            pattern_idx = 0
            compare_idx = compare_idx - pattern_idx + 1
    print(f'#{tc} {result}')
```