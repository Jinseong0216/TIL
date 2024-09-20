import sys
sys.stdin = open('input.txt')

def search(node):   # 해당 노드 정보를 토대로, 왼쪽, 오른쪽 조사
    if node != 0:   # 그 node 값이 0이 아니라면 (0번 노드는 없음.)
        search(tree[node][0])    # 왼쪽을 조사
        print(node)
        search(tree[node][1])    # 오른쪽을 조사

V = int(input())    # 전체 노드 수
# 1 2 3 4   공백을 기준으로 문자열이 오므로
arr = list(map(int, input().split()))
# tree 정보를 입력 할 수 있도록 하겠다.
# tree 리스트의 index 번호 -> 부모 노드의 번호
# tree[parent] 위치의 리스트의 0번째 -> 왼쪽 자식
# tree[parent] 위치의 리스트의 1번째 -> 오른쪽 자식
tree = [[0, 0] for _ in range(V+1)] # 0번노드 안쓸거니까
print(tree)
# # 부모 정보 입력을 위한
# parent = []
# # 왼쪽 자식 정보 입력을 위한
# left = []
# # 오른쪽 자식 정보 입력을 위한
# right = []
print(arr)
for i in range(len(arr) // 2): # 간선 정보
    # 부모, 자식 관계를 한번에 나타내고 싶음.
    parent = arr[i*2]
    child = arr[i*2+1]
    if tree[parent][0] == 0:    # 아직 왼쪽 자식 정보 기록한 적 없다면
        tree[parent][0] = child
    else:                       # 왼쪽 자식에 정보 넣었는데도, 또 자식이 있네?
        tree[parent][1] = child
                                # 아, 두번째 자식 오른쪽 자식도 필요하구나
print(tree)
search(1)