from collections import deque

class TreeNode:
    def __init__(self, key):
        self.key = key  # 노드의 값
        self.left = None  # 왼쪽 자식 노드를 가리킴
        self.right = None  # 오른쪽 자식 노드를 가리킴

class BinaryTree:
    def __init__(self):
        self.root = None  # 트리의 루트 노드

    # 새로운 노드를 삽입하는 함수 (레벨 순서 삽입)
    def insert(self, key):
        new_node = TreeNode(key)
        if self.root is None:
            self.root = new_node
            return

        # 레벨 순서로 트리를 탐색하기 위해 큐를 사용
        queue = deque([self.root])

        while queue:
            node = queue.popleft()

            # 왼쪽 자식이 비어있으면 삽입
            if node.left is None:
                node.left = new_node
                break
            else:
                queue.append(node.left)

            # 오른쪽 자식이 비어있으면 삽입
            if node.right is None:
                node.right = new_node
                break
            else:
                queue.append(node.right)

    def inorder_traversal(self):
        # 중위 순회를 통해 트리의 노드들을 출력하는 함수
        return self._inorder_traversal(self.root, [])

    def _inorder_traversal(self, node, result):
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.key)
            self._inorder_traversal(node.right, result)
        return result

# 예제 사용법
if __name__ == "__main__":
    tree = BinaryTree()
    tree.insert(50)
    print("Inorder Traversal:", tree.inorder_traversal())
    tree.insert(30)
    print("Inorder Traversal:", tree.inorder_traversal())
    tree.insert(20)
    print("Inorder Traversal:", tree.inorder_traversal())
    tree.insert(40)
    print("Inorder Traversal:", tree.inorder_traversal())
    tree.insert(70)
    print("Inorder Traversal:", tree.inorder_traversal())
    tree.insert(60)
    print("Inorder Traversal:", tree.inorder_traversal())
    tree.insert(80)

    print("Inorder Traversal:", tree.inorder_traversal())
