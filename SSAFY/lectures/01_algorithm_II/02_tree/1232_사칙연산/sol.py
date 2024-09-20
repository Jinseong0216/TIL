import sys
sys.stdin = open('input.txt')

def cal(left, right, oper):
    # print(f'{left} {oper} {right}', 'f-string')
    # print(eval(f'{left} {oper} {right}'), 'evaluation')
    return eval(f'{left} {oper} {right}')


def postorder(node):
    '''
        이번에는 트리를 구성할 때, 없는 자식 노드 번호는 기록하지 않앗다.
        [0, [1, '-', 2, 3], [2, '-', 4, 5], [3, 10], [4, 88], [5, 65]]
        왼쪽, 오른쪽 자식이 반드시 있는 경우가 있다.
        언제-> 연산자인 경우만 있다.
        arr[node][1] -> '+-*/'
    '''
    # if node:    # 노드가 있으면...
    # 시퀀스 연산자 -> 순서가 있는 자료형
        # if arr[node][1].isdecimal():  # 문자열 메서드 isdecimal
    if type(arr[node][1]) == type(''):
    # if arr[node][1] in '+-/*':
    # if arr[node][1] in ['+', '-', '*', '/']:   #  얘가 연산자임을 알 수 있는 방법은?
        left = postorder(arr[node][2])
        right = postorder(arr[node][3])
        # print(left, right)
        return cal(left, right, arr[node][1])
        # 연산을 줄줄줄..
    else:       # 저기 있는 저 연산자 목록에 포함이 안되는 값? 피연산자
        return arr[node][1]


for tc in range(1, 11):
    N = int(input())
    # node 번호 인덱스로 사용할 값만 int로 형변환 해서 tree 정보 기록
    arr = [list(map(lambda x: int(x) if x.isdecimal() else x, input().split())) for _ in range(N)]
    arr.insert(0, 0)    # 0번 노드는 사용하지 않을 것이므로, 0번째에 안쓸 값 삽입
    result = postorder(1)
    print(f'#{tc} {int(result)}')
