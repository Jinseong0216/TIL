import sys
sys.stdin = open('algo2_sample_in.txt')

def inorder(tree, node, idx):
    if node < 8:
        inorder(tree, node * 2, idx)
        # 내가 해야 할 일
        result[idx] += tree[node]
        inorder(tree, node * 2 + 1, idx)

# word : 조사 대상의 값
# idx : 조사 대상의 index
def push(word, idx):
    tree = [0] * 8
    last = 1    # 0번 노드와 0번 비트는 사용하지 않을 것이고
    while last < 8:
        tree[last] = word[last]
        last += 1
    # 조사 대상의 값으로 tree를 구성 완료했다면... 중위 순회
    # 중위 순회할 tree, 넘겨주기
    # 조사 대상의 시작 노드 넘겨주기
    # 조사 대상이 몇번째 조사 대상인지 같이 넘겨주기
    inorder(tree, 1, idx)

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = input()
    result = [''] * N
    for idx in range(N):  # 전수 조사
        # 전부 ASCII 코드로 변환 하고, 8비트 2진수로
        word = f"{ord(data[idx]):08b}"
        push(word, idx)
        # word를 각각의 tree에 적절히 삽입,
        # 결과물도, 각각의 원래 위치에 맞게 넣고 싶다면...?
    print(f'#{tc}', *result)
