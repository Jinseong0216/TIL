import sys
sys.stdin = open('input.txt')


for T in range(1, int(input())+1):
    N = int(input())
    root = 1
    nodes = [[0, 0] for _ in range(N+1)]
    while 2*root <= N:
        nodes[root][0] = 2*root
        if 2*root+1 <= N: nodes[root][1] = 2*root+1
        root = root+1

    order_list = [0]
    node_data = [0]*(N+1)

    def inorder(root):
        global order_list

        if root == 0: return

        inorder(nodes[root][0])
        order_list.append(order_list[-1]+1)
        node_data[root] = order_list[-1]
        inorder(nodes[root][1])

    root = 1
    inorder(root)
    print(f'#{T}', node_data[root], node_data[N//2])



