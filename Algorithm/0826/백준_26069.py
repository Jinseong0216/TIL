# 붙임성 좋은 총총이

info = {'ChongChong': 1}
for _ in range(int(input())):
    P, Q = input().split()
    if info.get(P, 0) or info.get(Q, 0): info[P], info[Q] = 1, 1
print(sum(info.values()))