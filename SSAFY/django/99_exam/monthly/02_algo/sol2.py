import sys
sys.stdin = open('algo2_sample_in.txt')

def inorder(node):
    global result
    if node < 8:
        inorder(node *2)
        result += tree[node]
        inorder(node * 2 + 1)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = input()
    for i in range(N):  # 전수 조사
        # 전부 ASCII 코드로 변환 하고, 8비트 2진수로
        tree = list(f"{ord(data[i]):08b}")
        result = '' # 각각의 문자를 8비트 2진수로 바꿔서. 중위순회 한 결과
        inorder(1)
        print(result, end=' ')
    print()
