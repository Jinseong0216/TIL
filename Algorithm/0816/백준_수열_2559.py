N, K = map(int, input().split())    # N=온도측정 길이, K=구해야하는 연속적인 날
temperature = list(map(int, input().split()))   # 온도 입력받기

result = []
idx = 0
while idx < N-K:
    if temperature[idx] > temperature[idx+K]:
        result.append(idx)
        idx += 2
    else:
        idx += 1

answer = sum(temperature[N-K-1:])
for idx in result:
    temp = sum(temperature[idx:idx+K])
    if answer < temp:
        answer = temp

print(answer)
