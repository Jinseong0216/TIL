decoder = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3,
           '0100011': 4, '0110001': 5, '0101111': 6, '0111011': 7,
           '0110111': 8, '0001011': 9}

for T in range(1, int(input())+1):
    # N, M 입력받기
    N, M = map(int, input().split())
    # 바코드 저장
    grid = [input().strip() for _ in range(N)]
    for idx in range(N):
        # 검사할 행
        row = grid[idx]
        for jdx in range(M-55):
            flag = -1
            # 해당 위치의 7자리 코드가 적절한 바코드라면
            if row[jdx:jdx+7] in decoder:
                flag, ans = 0, 0
                # 연속된 8개의 코드(7자리)에 대해서 검사 진행
                for weight in range(8):
                    code = row[jdx+7*weight:jdx+7*(weight+1)]
                    # 8개의 코드 묶음으로 분류 할 수 없는 경우
                    if code not in decoder:
                        flag = -1; break;
                    # 자리수가 홀수면 3배, 자리수가 짝수면 1배
                    flag += (2*((weight+1)%2)+1)*decoder[code]
                    ans += decoder[code]
                if flag != -1: break
        if flag != -1: break

    if flag%10 != 0 : print(f'#{T}', 0)
    else: print(f'#{T}', ans)

