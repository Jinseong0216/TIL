import sys
sys.stdin = open('input.txt')


# 연산을 실제로 수행하는 함수
def calculate(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        # 나눗셈의 경우 소수점 이하를 버림
        if a < 0:   # 단 음수에 대해서 별도 처리
            return -(-a // b)
        else:
            return a // b

def backtrack(idx, current_value):
    global max_result, min_result

    # 모든 연산자를 다 사용한 경우
    if idx == N - 1:
        max_result = max(max_result, current_value)
        min_result = min(min_result, current_value)
        return

    # 각 연산자를 사용해 탐색
    for i in range(4):
        if operator_count[i] > 0:  # 사용할 수 있는 연산자가 남아있다면
            operator_count[i] -= 1  # 해당 연산자를 사용
            next_value = calculate(current_value, numbers[idx + 1], operators[i])
            backtrack(idx + 1, next_value)  # 다음 숫자와 연산
            operator_count[i] += 1  # 연산자 복구 (백트래킹)


T = int(input())
operators = ['+', '-', '*', '/']  # 연산자 종류

for tc in range(1, T + 1):
    N = int(input())  # 숫자의 개수
    operator_count = list(map(int, input().split()))    # 각 연산자의 개수
    numbers = list(map(int, input().split()))            # 숫자들

    # 최댓값과 최솟값 초기화
    max_result = -float('inf')
    min_result = float('inf')

    # 백트래킹 시작
    backtrack(0, numbers[0])

    # 결과 출력
    print(f"#{tc} {max_result - min_result}")
