import sys
sys.stdin = open("input.txt")

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

for tc in range(int(input())):
    N = int(input())  # N: 스위치 개수
    switch = [0] + list(map(int, input().split()))  # 스위치 상태
    S = int(input())  # S: 학생 수
    student = [tuple(map(int, input().split())) for _ in range(S)]  # 성별, 받은 수

    for gen, num in student:
        if gen == 1:  # 남자이면
            for i in range(2, N+1):
                if is_prime(i):
                    switch[i] = 1 - switch[i]
                    for j in range(1, num+1):
                        if i + j <= N:
                            switch[i + j] = 1 - switch[i + j]
                        if 0 <= i - j:
                            switch[i - j] = 1 - switch[i - j]
        else:  # 여자이면
            for i in range(1, N+1):
                if num % i == 0:
                    switch[i] = 1 - switch[ i]

    print(f'#{tc+1}')
    for k in range(1, N+1):
        print(switch[k], end=" ")
        # 20줄이 넘어가면 줄바꿈
        if k % 20 == 0:
            print()
    print()

'''
<부록 : 소수 쉽게 구하기 - 에라토스테네스의 체>

1. 2부터 소수를 구하고자 하는 구간의 모든 수를 나열
2. 2는 소수이며, 자기 자신을 제외한 2의 배수를 모두 지움
3. 3은 소수이며, 자기 자신을 제외한 3의 배수를 모두 지움
4. 원하는 구간이 n이라면, sqrt(n) 이하의 소수에 대해 반복
5. 남는 수는 모두 소수
'''