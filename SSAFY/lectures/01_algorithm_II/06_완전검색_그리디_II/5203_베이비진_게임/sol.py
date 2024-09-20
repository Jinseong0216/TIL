import sys
sys.stdin = open('input.txt')

def search(arr, num):
    '''
        arr : A or B 배열을 넘겨받아, 각각 카운팅
        num : 삽입할 카드번호
    '''
    arr[num] += 1       # 카드 카운팅 증가 후,
    if arr[num] == 3:   # 해당 카드가 3장이 되었다면 승.
        return 1
    for i in range(8):          # 0~2, 1~3 ... 7~9 까지 3장씩 연달아 있는지 확인
        if all(arr[i:i+3]):     # all([0, 0, 1]) == False / all([1, 1, 1] == True
            return 1

T = int(input())

for tc in range(1, T+1):
    data = list(map(int, input().split()))
    A_arr = [0] * 10    # 0~9 카드 카운팅용 배열 A
    B_arr = [0] * 10    # 0~9 카드 카운팅용 배열 B
    A, B = 0, 0         # 승자 판별용
    result = 0          # 무승부시 0 출력
    for idx in range(len(data)):    # 카드 삽입
        if idx % 2:     # 홀수 번째 -> 1, 3, 5... index라면 B 차례
            B = search(B_arr, data[idx])    # 카드 추가 후, 베이비진 판별
        else:           # 짝수 번째 -> 0, 2, 4... index라면 A 차례
            A = search(A_arr, data[idx])    # 카드 추가 후, 베이비진 판별
        # 이번 idx 차례에 A든, B든 누구라도 1로 변경되었다면
        # search 함수의 반환값 1을 받았다는 것이 되므로 해당 유저가 승자.
        if A:
            result = 1      # 출력 결과 변환 후,
            break           # 조사 종료.
        if B:
            result = 2
            break
    print(f'#{tc} {result}')