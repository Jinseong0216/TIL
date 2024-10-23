def operating_price(K):
    if K < 1: return 0
    else: return pow(K, 2) + pow(K-1, 2)

# 방범 범위 안에 있는지 계산
def number_of_house_in_distance(i, j):    
    temp_cnt = 0
    for idx in range(low_bnd_of_idx, upper_bnd_of_idx+1):
        for jdx in range(low_bnd_of_jdx, upper_bnd_of_jdx+1):
            if abs(i-idx) + abs(j-jdx) >= K: continue
            if downtown[idx][jdx] == 0: continue
            temp_cnt += 1
    return temp_cnt


for test_case in range(1, int(input().strip())+1):
    N, M = map(int,input().split())
    # 마을의 정보 받아오기
    downtown = list(list(map(int,input().split())) for _ in range(N))
    # 집의 위치 저장    
    profit, cnt, K = 0, 0, N*2

    while K > 0:
        op_price = operating_price(K)
        if cnt*M >= op_price: break
        
        for i in range(N):
            for j in range(N):
                low_bnd_of_idx, upper_bnd_of_idx = max(0, i-N), min(i+K-1, N-1)
                low_bnd_of_jdx, upper_bnd_of_jdx = max(0, j-N), min(j+K-1, N-1)
                temp_cnt = number_of_house_in_distance(i, j)
                # 적자인 경우
                if temp_cnt*M < op_price: continue
                if cnt >= temp_cnt: continue
                cnt = temp_cnt

        K -= 1
    print(f'#{test_case} {cnt}')