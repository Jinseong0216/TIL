import sys
input = sys.stdin.readline

def 약수찾기(자연수):
    소인수분해 = {}
    for 약수후보 in range(2, 자연수+1):
        if 자연수 % 약수후보 != 0: continue
        약수 = 약수후보
        소인수분해[약수] = 소인수분해.get(약수, 0)

        while 자연수 % 약수 == 0:
            소인수분해[약수] = 소인수분해[약수]+1
            자연수 = 자연수//약수
    
    if 소인수분해 == {}: 
        소인수분해 = {자연수: 1}
    return 소인수분해

문제수 = int(input().strip())
for 문제번호 in range(1, 문제수+1):
    자연수_A, 자연수_B = map(int, input().split())
    약수개수_A, 약수개수_B = 약수찾기(자연수_A), 약수찾기(자연수_B)

    소인수분해_A = set(약수개수_A.keys())
    소인수분해_B = set(약수개수_B.keys())
    소인수들 = 소인수분해_A.union(소인수분해_B)

    최소공배수 = 1
    for 소인수 in 소인수들:
        최소공배수 *= 소인수**max(약수개수_A.get(소인수, 1), 약수개수_B.get(소인수, 1))
    print(최소공배수)