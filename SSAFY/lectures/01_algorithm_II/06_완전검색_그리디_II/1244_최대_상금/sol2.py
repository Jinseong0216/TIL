import sys
sys.stdin = open('input.txt')

def swap(cards, i, j):
    # i와 j 위치의 숫자를 교환하여 새로운 숫자를 반환
    card_list = list(cards)     # 단, 문자열은 immutable 하므로 list로 변환
    card_list[i], card_list[j] = card_list[j], card_list[i]     # 스왑
    return ''.join(card_list)   # 다시 문자열로 반환



# cards : 순열 대상
# now : 현재 조사 위치
# r : 최대 조사 횟수 (최대 교환 횟수)
def perm(cards, now, r):
    global result
    # 내가 만들수있는 모든 경우의 수에 대해서
    for i in range(720):
        # now번 swap 했을때, i번쨰 경우의 수에 올 수 있는 수가
        # 아직 기록되지 않았다면
        if memo[now][i] == 0:
            memo[now][i] = cards
            break
        elif memo[r][i] == cards:
            return

    if now == r:    # 내 조사 횟수가 최대 조사 횟수와 동일해졌다
        # 최댓값 갱신
        if int(cards) > result:
            result = int(cards)
    else:
        for i in range(N - 1):
            for j in range(i + 1, N):
                new_card = swap(cards, i, j)
                perm(new_card, now + 1, r)




T = int(input())
for tc in range(1, 3):
    cards, r = input().split()
    r = int(r)
    N = len(cards)
    # R번째일때, 만들어질 수 있는 최대 경우의수를 모두 기록할 수 있는 리스트
    # arr = 123
    # index == 0 : 한번도 교환 안한 경우
    # 최대 교환 횟수가 10
    # 1번째일떄 만들어질 수 있는 경우의수
    # 각 횟수차 마다 들갈수있는 최대의 경우의수
    # 순열의 경우 N에 대한 모든 경우의수 가 N! 최대 N - > 6
    memo = [[0] * 720 for _ in range(11)]
    result = 0
    perm(cards, 0, r)
    for m in memo:
        if any(m):
            print(m)
    print(f'#{tc} {result}')



