# 아래와 같이 예외를 작성하면 코드는 2번째 except 절에 이후로 도달하지 못함
# ZeroDivisionError 클래스는 BaseException 클래스의 하위 클래스 중 하나이므로 ZeroDivisionError를 먼저 작성해야 함
try:
    num = int(input('100으로 나눌 값을 입력하시오 : '))
    print(100 / num)
except BaseException:
    print('숫자를 넣어주세요.')
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except:
    print('에러가 발생하였습니다.')
