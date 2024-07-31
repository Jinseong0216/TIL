# 버블 정렬 연습

def BubbleSort(arr, N):
    for i in range(N-1):
        for j in range(i, N-1):
            x, y = arr[j], arr[j + 1]
            if x > y:
                arr[j], arr[j+1] = y, x
    return arr

sorted_arr = BubbleSort([55, 7, 78, 12, 42], 5)
print(sorted_arr)

seq = list(map(int, input().split()))
N = len(seq)

for i in range(N):
    for j in range(i, N-1):
        x, y = seq[j], seq[j+1]
        if x > y:
            seq[j], seq[j+1] = y, x
print(seq)

N = 6
arr = [7, 2, 5, 3, 4, 1]

for i in range(N-1, 0, -1):
    for j in range(i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr)
