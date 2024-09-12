import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

start = (1,3)
que = deque([start])
ans = 0

i, j = que.popleft()

