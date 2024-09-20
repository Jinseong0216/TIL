import sys
sys.stdin = open('input.txt')

def merge_sort(div_arr):
    global result

    if len(div_arr) <= 1:
        return div_arr

    mid = len(div_arr) // 2             # 파티션을 나눌 기준점 설정
    left = merge_sort(div_arr[:mid])    # 기준점 왼쪽 전부
    right = merge_sort(div_arr[mid:])   # 기준점을 포함한 오른쪽 전부

    # 왼쪽과 오론쪽 배열의 각각 비교 대상과
    # 실제 배열에 값을 삽입할 위치 k
    left_idx, right_idx, k = 0, 0, 0

    # 범위를 벗어나지 않는 선에서
    while left_idx < len(left) and right_idx < len(right):
        # 오름 차순 정렬
        if left[left_idx] < right[right_idx]:
            div_arr[k] = left[left_idx]
            left_idx += 1
        else:
            div_arr[k] = right[right_idx]
            right_idx += 1
        k += 1

    # 왼쪽 배열이나, 오른쪽 배열 중 한 쪽이라도 조사를 끝냈다면
    # 아직 반대쪽 배열에는 값이 남아 있을 것이므로, 다 털어넣기.
    if left_idx < len(left):
        div_arr[k:] = left[left_idx:]
    if right_idx < len(right):
        div_arr[k:] = right[right_idx:]

    # 문제 요구 사항.
    if left[-1] > right[-1]:
        result += 1
    return div_arr

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))

    result = 0
    arr = merge_sort(data)
    print(f'#{tc} {arr[N//2]} {result}')

