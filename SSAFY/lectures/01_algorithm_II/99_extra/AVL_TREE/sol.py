class Node:
    def __init__(self, key):
        self.key = key
        self.height = 1     # 최초 루트 노드 높이 1
        self.left = None
        self.right = None

class AVL_TREE:
    # 핵심!
    # 높이를 계산 할 수 있어야 한다.
    # 높이 조회
    def get_height(self, node):
        # 왼쪽 자식, 오른쪽 자식 등... 없는 노드에 대한 처리
        if not node:
            return 0
        return node.height  # 노드의 높이 반환

    # 노드 업데이트를 위한 메서드
    def update_height(self, node):
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    # 균형 계수 계산 메서드
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    # 왼쪽 회전 (RR)
    def rotate_left(self, node):
        y = node.right  # y를 기존 노드의 오른쪽 자식들
        t = y.left      # y의 왼쪽 서브트리를 t로 설정
        # 좌회전
        y.left = node
        node.right = t
        self.update_height(node)
        self.update_height(y)
        return y

    # 오른쪽 회전
    def rotate_right(self, node):
        y = node.left
        t = y.right

        y.right = node
        node.left = t
        self.update_height(node)
        self.update_height(y)
        return y

    # 삽입
    def insert(self, node, key):
        if not node:
            return Node(key)    # 노드가 없으면 새 노드 인스턴스 생성 후, 반환

        # 기본적인 이진 탐색 트리 삽입
        if key < node.key:
            node.left = self.insert(node.left, key)
        elif key > node.key:
            node.right = self.insert(node.right, key)
        else:       # 현재 노드의 값이랑 중복되는 값은 어떻게 처리하나요?
            return node # 중복 키는 삽입하지 않겠습니다.

        self.update_height(node)
        # 균형 계수 맞는지...
        balance = self.get_balance(node)

        # 균형이 맞지 않는 경우,,, 처리해야한다.
        # LL
        if balance > 1 and key < node.left.key:
            return self.rotate_right(node)

        # RR
        if balance < -1 and key > node.right.key:
            return self.rotate_left(node)

        # LR
        if balance > 1 and key > node.left.key:
            node.left = self.rotate_left(node.left)
            return self.rotate_left(node)

        # RL
        if balance < -1 and key < node.right.key:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def inorder(self, node):
        if node:
            print(node.key, end=' ')
            self.inorder(node.left)
            self.inorder(node.right)

avl_tree = AVL_TREE()
root = None
keys = [10, 5, 15, 20]
for key in keys:
    root = avl_tree.insert(root, key)

# avl_tree.inorder(root)
avl_tree.insert(root, 30)
avl_tree.inorder(root)






