for tc in range(1, int(input())+1): # 테스트 케이스의 수
    N = int(input())
    d = 1
    while True:
        # 세제곱 값 계산
        ddd = pow(d, 3)
        # 같다면 출력
        if ddd == N: print(f'#{tc}', d); break;
        # 더 크다면 중지
        elif ddd > N: print(f'#{tc} -1'); break;
        # d값 1 증가
        d = d+1