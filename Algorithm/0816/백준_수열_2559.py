# import random
# N, K = 1000000, 3400
# temperature = [random.randint(-100, 100) for _ in range(1000)]
# #N, K = map(int, input().split())    # N=온도측정 길이, K=구해야하는 연속적인 날
# #temperature = list(map(int, input().split()))   # 온도 입력받기
# answer = sum(temperature[:K])
# for idx in range(1, N-K+1):
#     answer = max(answer, sum(temperature[idx: idx+K]))
# print(answer)



