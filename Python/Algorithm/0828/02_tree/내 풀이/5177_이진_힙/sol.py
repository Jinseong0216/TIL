import sys
sys.stdin = open('input.txt')

def enqueue(value, node):
    heap.append(value)
    parent = node//2
    while parent:
        if heap[node] <= heap[parent]:
            heap[parent], heap[node] = heap[node], heap[parent]
            node = parent
            parent = node//2
        else: break

for T in range(1, int(input())+1):
    N = int(input())
    heap, last = [0], 1
    for value in list(map(int, input().split())):
        enqueue(value, last)
        last = last+1


    ans = 0
    # last값 마지막에 1 더해진 상태인 걸 인지하고 있어야함!
    parent = ((last-1))//2
    while parent:
        ans += heap[parent]
        parent = parent//2
    print(heap)
    print(f'#{T}', ans)
