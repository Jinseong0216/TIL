'''# 백준 괄호추가하기
N = int(input())
nums = (N+1)//2
최대괄호_수 = num // 2

M = 

nums = 4
12      12 34


23 끝

34     

13 



1. 괄호 넣기

2. 끝에 수가 1개 남은 경우, 해당 수 제거 & 이후의 결과값에 항상 더해주면 됨'''


def cal(equ):
    if len(equ) > 3:
        equ = str(cal(equ[:3])) + equ[3:]
    else:
        if equ[1] == '*': return int(equ[0]) * int(equ[2])
        elif equ[1] == '+': return int(equ[0]) + int(equ[2])
        else: return int(equ[0]) - int(equ[2])


result = []
def main(equation, len_equation):
    if len_equation == 1: return int(equation)

    elif len_equation == 3: return cal(equation)

cal('5')

