def preorder(node):
    if node == 0: return

    print(node, end=' ')
    preorder(left[node])
    preorder(right[node])


N = int(input())
arr =list(map(int, input().split()))
left = [0]*(N+1)    # 왼쪽 자신 번호를 저장할 리스트
                    # ex) left[3]==2: 3번 부모의 왼쪽 자식은 2다.
right = [0]*(N+1)

for i in range(0, len(arr), 2):
    parent, child = arr[i], arr[i+1]
    # 왼쪽에 자식이 없다면, 왼쪽에 삽입
    if left[parent] == 0: left[parent] = child
    # 오른쪽 자식이 없다면
    else: right[parent] = child

root = 1 # 시작점은 1이다라고 가정.
preorder(root)

