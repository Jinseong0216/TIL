import sys
sys.stdin = open('input.txt')

password = {
    (2, 1, 1): 0,
    (2, 2, 1): 1,
    (1, 2, 2): 2,
    (4, 1, 1): 3,
    (1, 3, 2): 4,
    (2, 3, 1): 5,
    (1, 1, 4): 6,
    (3, 1, 2): 7,
    (2, 1, 3): 8,
    (1, 1, 2): 9,
}


def search(target):
    numbers = []    # 전체 수를 저장
    for i in range(0, len(target), 7):  # 암호 하나당 7글자이므로 7글자씩 떼어서
        current = target[i:i + 7]       # 해당 값에 대해
        count_list = []
        count = 1                       # 첫 개수는 건너뛰고 조사

        for j in range(1, 7):           # 2번째 값부터 조사
            '''
            j == 1 일때, 1번째와 0번째가 동일한지 체크
            001110011
             ↑
            001110011
            ↑ 
            '''
            if current[j] == current[j - 1]:    # 이전 수와 현재 수가 같다면
                count += 1                      # 동일한 수가 반복된 횟수 체크
            else:
                count_list.append(count)        # 다르다면, 지금까지 센 수를 추가하고
                count = 1                       # 개수를 다시 초기화
        count_list.append(count)                # 마지막까지 조사를 마쳤다면, 그때까지 센 수를 추가
        numbers.append(password[tuple(count_list[1:])]) # 암호 패턴에 맞춰 복호화 값을 추가

    result = sum(numbers[i] if i % 2 else numbers[i] * 3 for i in range(8))

    if result % 10 == 0:
        return sum(numbers)
    else:
        return 0


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]   # 우선 입력 받은 후

    result = None       # 아직 답을 찾기 전,
    for line in arr:    # 각 라인에 대해
        if '1' in line:  # 암호가 존재하는 행만 처리
            idx = line.rfind('1')   # 오른쪽에서부터 1을 찾아서 해당 위치 반환
            if idx >= 55:  # 암호의 최소 길이가 56이므로
                result = search(list(map(int, line[idx - 55:idx + 1]))) # 암호 부분만 떼어서 계산
                if result != None:      # 값을 한 번 이라도 찾았다면 종료
                    break

    print(f'#{tc} {result}')

