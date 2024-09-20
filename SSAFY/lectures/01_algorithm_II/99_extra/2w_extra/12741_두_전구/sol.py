import sys
sys.stdin = open('input.txt')

T = int(input())
answer = ''
for tc in range(1, T+1):
    A, B, C, D = list(map(int, input().split()))
    result = max(min(B, D) - max(A, C), 0)
    answer += f'#{tc} {result} \n'  # 출력에 시간이 소비되어... 한번에 합쳐서 출력.
print(answer)