'''
sequence 정렬
+
이진탐색
10만 x 16 = 160만
    ... 대략적으로 200만번 연산 들어감

=> 정렬 연산횟수 + 이진탐색 연산횟수

'''
def is_in(num, target_sequence, start, end):
    global ans

    middle = (start+end)//2
    middle_num = target_sequence[middle]

    if num == middle_num: 
        ans = 1
        return None
    
    if start > end:
        ans = 0
        return None
    
    if num < middle_num: end = middle-1
    
    elif num > middle_num: start = middle+1
    
    return is_in(num, target_sequence, start, end)


N = int(input().strip())
sequence = sorted(list(map(int, input().split())))
M = int(input().strip())
arr = list(map(int, input().split()))

for num in arr:
    ans = 0
    is_in(num, sequence, 0, N-1)
    print(ans)