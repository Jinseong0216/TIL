import sys
sys.stdin = open('input.txt')

def quick_sort(div_arr):
    if len(div_arr) <= 1:
        return div_arr
    else:
        pivot = div_arr[0]
        left, equal, right = [], [], []
        for i in range(len(div_arr)):
            if div_arr[i] < pivot:
                left.append(div_arr[i])
            elif div_arr[i] == pivot:
                equal.append(div_arr[i])
            else:
                right.append(div_arr[i])
        return [*quick_sort(left), *equal, *quick_sort(right)]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    result = quick_sort(data)
    print(f'#{tc} {result[N//2]}')