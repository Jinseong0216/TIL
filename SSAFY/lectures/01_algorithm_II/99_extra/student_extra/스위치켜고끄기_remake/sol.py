import sys
sys.stdin = open('input.txt')

# 소수 판단 함수
def is_prime(number):
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 1: on, 2: off
    data = list(map(int, input().split()))
    S = int(input())
    # 1: man, 2: woman | switch num
    students = [list(map(int, input().split())) for _ in range(S)]

    for s in students:
        type, num = s
        if type == 1:   # 남자일 때,
            for n in range(1, N+1):
                if is_prime(n):     # 스위치 번호가 소수이면
                    data[n - 1] = int(not data[n - 1])
                    for k in range(1, num+1):
                        left = n - k - 1
                        right = n + k - 1
                        if 0 <= left:
                            data[left] = int(not data[left])
                        if right < N:
                            data[right] = int(not data[right])
        else:
            for n in range(1, num+1):
                if not num % n:
                    data[n - 1] = int(not data[n - 1])

    data.insert(0, 0)
    print(f'#{tc}')
    for i in range(1, len(data)):
        print(data[i], end=' ')
        if not i % 20:
            print()
    print()