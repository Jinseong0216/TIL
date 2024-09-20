import sys
sys.stdin = open('input.txt')


def search(node):
    global result
    if node:    # 노드가 존재하면
        search(arr[node][2])   # 2번 인덱스가 왼쪽 자식
        # 중위 순회이므로 이곳에서 result에 V 를 더해줌
        result += arr[node][1]
        search(arr[node][3])    # 3번 인덱스가 오른쪽 자식

for tc in range(1, 11):     # 총 10개의 TC
    N = int(input())        # 노드의 개수
    # 아래 코드에 대해서 pythonic 하게 코드 줄이기
    # 딱히 가독성이 좋지는 않음.
    arr = [list(map(lambda x: int(x) if x.isdecimal() else x, input().split())) for _ in range(N)]
    # 노드의 개수 만큼 반복해서 정보 삽입
    # 단, int로 변환 불가능한 'W' 등이 있으므로 split만 해주고 삽입
    arr = [input().split() for _ in range(N)]
    # print(arr)    # 출력 결과 확인

    '''
    arr의 모양새는 다음과 같다.
            0 -> 인덱스 정보가 부모 노드의 정보와 동일
       P    V    LC   RC
    [['1', 'W', '2', '3'],
    P : 부모
    V : 값
    LC : 왼쪽 자식 노드 번호
    RC : 오른쪽 자식 노드 번호
    위 구조를, tree의 구조가 되도록 변경
        1. LC, RC의 값이 정수가 되어야 index 로 사용가능
        2. LC, RC 중 하나라도 값이 비어있으면 순회에 문제 발생
            - 따라서 자식이 없는 경우 0으로 채워주기 
    '''
    for node_info in arr:
        for idx in range(len(node_info)):
            # if node_info[idx] in '0123456789':  # 노드번호가 2자리수면.. 곤란할지도...
            if node_info[idx].isdecimal():  # 정수로 변환 가능하다면
                node_info[idx] = int(node_info[idx])
    # print(arr)    # 정수로 변환됨 확인.
    for node_info in arr:
        while len(node_info) != 4:  # 모든 정보가 없다면
            node_info.append(0)     # 자식 없음을 추가
    # print(arr)      # 전처리 완료됨을 확인
    # 0번 노드 정보가 없으므로 삽입
    arr.insert(0, [0, 0, 0, 0])
    # 최종 출력 값
    result = ''
    # 중위 순회
    search(1)   # 1번 노드부터 순회
    print(f'#{tc} {result}')

