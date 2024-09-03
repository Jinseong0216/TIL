# 5201. [파이썬 S/W 문제해결 구현] 3일차 - 컨테이너 운반

for T in range(1, int(input())+1): # 테스트케이스
    N, M = map(int, input().split()) # 화물 개수, 트럭의 수
    weights = list(map(int, input().split())) # 화물 무게
    weights_list = [0]*51 # 화물 무게
    for weight in weights: weights_list[weight] += 1
    trucks = sorted(map(int, input().split())) # 트럭 적재용량

    ans = 0
    for truck in trucks:
        # 트럭무게와 같은 화물부터 검사
        for idx in range(truck, 0, -1):
            # 트럭무게와 같거나 작은 화물중에서 가장 큰 화물을 찾는 것임
            if weights_list[idx]:
                # 해당화물이 있으면 개수 -1 
                weights_list[idx] -= 1
                # 화물의 무게를 더해주고
                ans += idx
                # 반복문 중단
                break
    print(f'#{T}', ans)






