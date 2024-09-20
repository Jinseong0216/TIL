import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    data = input()
    '''
        AABC... 와 같은 형태 일때,
        stack에는 조사 대상의 값을 삽입한다.
        
        stack = []
        i = 0 -> data[i] = 'A'
        AABC
        ↑
        이때, stack이 비어있으므로 조사 대상이 없다.
        그렇다면 즉시 stack에 값 삽입
        stack = ['A']
        
        ---
        
        stack의 마지막 요소가 지금 조사 대상과 동일한 경우
        stack = ['A']
        i = 1 -> data[i] = 'A' 
        AABC
         ↑
        stack[-1] == data[i]
        중복되는 문자열인 경우, stack에서 해당 값을 제거한다.
        stack = []
    '''
    # 위와 같은 규칙을 위해 코드를 작성하려고 할 때,
    # 최초 삽입 대상. 즉, i가 0인 경우엔, stack의 -1 번째가 존재하지 않으므로 indexError가 발생.
        # 애초에 중복 되는지 확인 할 대상인 `이전 요소` 가 존재하지 않으므로
        # stack이 비어있는 경우에는 무조건 값을 삽입해야 함에 주의

    stack = []  # stack 초기화
    # for i in range(len(data)):   # data 전수조사
    #     if not stack:                   # stack이 비었다면
    #         stack.append(data[i])       # 무조건 값을 삽입하고
    #         continue                    # 아래 코드를 실행하지 않고, 다음 조사 대상으로 넘긴다.
    #     # stack이 비지 않았는데,
    #     if data[i] == stack[-1]:        # 현재 조사 대상이 stack의 마지막 값과 같다면,
    #         stack.pop()                 # 중복되는 대상을 stack에서 삭제한다.
    #     # stack이 비지도 않았고, 마지막 값이랑 같지도 않으면
    #     else:
    #         stack.append(data[i])       # stack에 값을 삽입한다.

    # 위 코드에서 중복되는 부분 (stack.append(data[i]) 부분을 줄이기 위해 로직을 바꿔보자.
    for i in range(len(data)):
        if stack:                       # stack에 값이 있다면,
            if data[i] == stack[-1]:    # 비교 할 수 있으므로 비교 후, 중복되면
                stack.pop()             # stack의 마지막 값 제거
                continue                # 아래 코드를 실행하지 않고 다음 조사
        '''
            stack이 비어 있었다면, 
            첫번째 조건문 if stack 의 결과가 False로 아래 코드 실행
            
            stack이 비어 있지는 않았지만,
            if data[i] == stack[-1] 의 결과가 False 인경우,
            즉, stack의 마지막과 data[i] 번째가 같지 않은 경우, 
            continue가 실행되지 않았으므로,
            아래 코드 실행
        '''
        stack.append(data[i])       # 해당 조사 대상 삽입.
    print(f'#{tc} {len(stack)}')
