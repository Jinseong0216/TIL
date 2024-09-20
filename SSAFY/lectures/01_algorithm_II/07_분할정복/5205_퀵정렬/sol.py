import sys
sys.stdin = open('input.txt')

def quick_sort(div_arr):
    if len(div_arr) <= 1:
        return div_arr
    else:
        pivot = div_arr[0]  # 왼쪽을 피봇으로 잡음.
        left, right = [], []
        for i in range(1, len(div_arr)):
            if div_arr[i] < pivot:
                left.append(div_arr[i])
            else:
                right.append(div_arr[i])
        return [*quick_sort(left), pivot, *quick_sort(right)]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = quick_sort(arr)
    print(result)
    # print(f'#{tc} {sorted(arr)[N//2]}')