def divide(x, y):
    if x < 0 and y > 0: return -((-x)//y)
    return x // y

def dfs(order, val, operators):
    global min_val, max_val
    # 마지막 연산자에 도달하였다면
    if order == N-1:
        # 결과 업데이트
        if min_val > val: min_val = val
        if max_val < val: max_val = val
        # 종료
        return

    for i in range(4):
        if operators[i] == 0: continue
        operators[i] -= 1
        # 더하기
        if i == 0: 
            dfs(order+1, val+arr[order+1], operators)
        # 빼기
        elif i == 1: 
            dfs(order+1, val-arr[order+1], operators)
        # 곱하기
        elif i == 2: 
            dfs(order+1, val*arr[order+1], operators)
        # 나누기
        else:
            dfs(order+1, divide(val,arr[order+1]), operators)
        operators[i] += 1
        
if __name__ == "__main__":
    N = int(input())
    # 배열, 연산자 개수
    arr, operators = list(map(int, input().split())), list(map(int, input().split()))
    # 초기값 설정
    min_val, max_val = float('inf'), float('-inf')
    # 함수 호출
    dfs(0, arr[0], operators)
    print(max_val)
    print(min_val)