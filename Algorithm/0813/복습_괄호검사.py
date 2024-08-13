T = int(input())
for t in range(1, T+1):
    sentence = list(input())
    parenthesis = {')': '(', '}': '{'}
    stack = []
    ans = 1
    for element in sentence:
        if element == '(' or element == '{': stack.append(element)
        elif element == ')' or element == '}':
            if stack and stack[-1] == parenthesis[element]: stack.pop()
            else: ans = 0

    if stack: ans = 0
    print(f'#{t} {ans}')