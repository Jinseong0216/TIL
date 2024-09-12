def cut(command, arr):
    direct, branch = command
    result = []
    for rec in arr:
        if direct == 0:
            if (rec[0][0] < branch < rec[1][0]):
                result += [[rec[0], [branch, rec[1][1]]], [[branch, rec[0][1]], rec[1]]]
            else:
                result += [rec]
        if direct == 1:
            if (rec[0][1] < branch < rec[1][1]):
                result += [[rec[0], [rec[1][0], branch]], [[rec[0][0], branch], rec[1]]]
            else:
                result += [rec]
    return result


width, height = map(int, input().split())   # 가로, 세로
rectangle = [[[0, 0], [height, width]]]
N = int(input())    # 명령어의 수
for _ in range(N):
    command = list(map(int, input().split()))
    rectangle = cut(command, rectangle)

answer = 0
for rec in rectangle:
    [[a, b], [c, d]] = rec
    answer = max((d-b)*(c-a), answer)
print(answer)