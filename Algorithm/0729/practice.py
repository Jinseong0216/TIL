# Solving Club: List1
# [D3] 4831. [파이썬 S/W 문제해결 기본] 1일차 - 전기버스

# for t in range(1, int(input())+1):
#     K, N, M = map(int, input().split())            
#     chargers = list(map(int, input().split()))     
#     cnt = 0

#     if max(chargers[i+1] - chargers[i] for i in range(len(chargers)-1)) > K: 
#         print(f'#{t}', cnt)
    
#     else:
#         i = 0                                               
#         while i < N + 1:
#             if i+K >= N: break
#             else:
#                 i = max(charger for charger in chargers if i+K >= charger)
#                 cnt += 1
#         print(f'#{t}', cnt)





# Solving Club: List1
# [D2] 21436. 4835. [파이썬 S/W 문제해결 기본] 1일차 - 구간합
# 
# for t in range(1,int(input())+1):

#     N, M = map(int, input().split())
#     seq = list(map(int, input().split()))
#     min_max = [sum(seq[:M])] * 2

#     for i in range(1, N-M+1):
#         min_max = [min(min_max[0], sum(seq[i:i+M])), max(min_max[1], sum(seq[i:i+M]))]

#     print(f'#{t}', min_max[1]-min_max[0])






# Solving Club: List1
# [D2] 21435. 4834. [파이썬 S/W 문제해결 기본] 1일차 - 숫자 카드

T = int(input())
for t in range(1, 2):
    N = int(input())
    numbers = [int(num) for num in input()]
     
    ans = [(numbers.count(num), num) for num in range(10)]
    ans.sort(key = lambda x: (x[0], -x[1]))

    print(f'#{t}' ,ans[-1][1], ans[-1][0])
    