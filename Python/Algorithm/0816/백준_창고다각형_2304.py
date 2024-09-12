N = int(input()) # 기둥의 개수
height = [0]*(1000+2)
# 기둥 위치와 높이를 height 리스트에 표시
max_height = branch = 0
for _ in range(N):
    x, h = map(int, input().split())
    height[x] = h
    # 최대높이와 그 기둥의 위치 찾기
    if max_height < h: max_height, branch = h, x

def fnct():
    global height

    idx = jdx = 0
    while idx < 1002:
        if height[idx] == 0:
            idx, jdx = idx+1, jdx+1
            continue
        jdx = idx+1
        while jdx < 1002:
            if height[jdx] < height[idx]: jdx += 1
            else:
                height[idx+1:jdx] = [height[idx]]*(jdx-idx-1)
                idx = jdx
                break
        if jdx == 1002: break
    return

fnct(); height = height[::-1]; fnct()
print(sum(height))