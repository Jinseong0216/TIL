import sys
sys.stdin = open('input.txt')

def swap(cards, i, j):
    # i와 j 위치의 숫자를 교환하여 새로운 숫자를 반환
    card_list = list(cards)     # 단, 문자열은 immutable 하므로 list로 변환
    card_list[i], card_list[j] = card_list[j], card_list[i]     # 스왑
    return ''.join(card_list)   # 다시 문자열로 반환

def perm(cards, now, r):
    global result, visited
    if now == r:                    # 기저 도달시
        if int(cards) > result:     # 크기 비교를 위해 int로 변환후.
            result = int(cards)     # 최댓값 갱신
        return

    for i in range(N - 1):          # 0부터 N-1까지
        for j in range(i + 1, N):   # i번째 다음부터 마지막까지
            new_cards = swap(cards, i, j)   # 원본을 스왑한 결과로
            if (new_cards, now + 1) not in visited:     # 해당 회차 스왑 결과에 중복이 없다면
                visited.add((new_cards, now + 1))       # 회차 정보와 스왑 결과를 같이 삽입하고
                perm(new_cards, now + 1, r)             # 다음 회차 스왑 작업 조사

T = int(input())
for tc in range(1, T + 1):
    # 데이터, 스왑 횟수
    cards, r = input().split()
    r = int(r)
    N = len(cards)  # 전체 카드 길이
    result = 0      # 최종 결괏값
    '''
        123을 2번 swap 한다면,
        각 swap 회차별 생성 가능한 순열
        1 :         213     |      321     |      132       : 중복 없음
        2 :     123 312 231 |  231 123 312 |  312 231 123   : 123, 312, 231 이 중복되어서 나타난다.
           
        1번째 스왑으로 얻은 결과 213에서 만들어진 
        2번째 스왑 결과 123
         
        1번째 스왑으로 얻은 결과 321에서 만들어진 
        2번째 스왑 결과 123
        
        위 2상황은 3번째 스왑 결과에 아무런 영향을 미치지 않는 중복된 결괏값이 된다.
        따라서 동일 스왑 횟수에 동일 값에 대해서는 중복을 제거한다.
        
        이를 위해 visited를 set으로 선언.         
    '''
    visited = set()     # 중복된 결과 제거용 set type visited
    perm(cards, 0, r)   # 0번째부터 전체 스왑 횟수까지 작업 진행
    # print(visited)
    print(f'#{tc} {result}')
