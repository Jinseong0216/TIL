############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 반드시 재귀 함수 형태로 구현해야 합니다.
def reverse_string(s):
    if len(s) == 0:                             # 탈출 조건 지정(문자열의 길이가 0)
        return ''
    else:
        return s[-1] + reverse_string(s[:-1])   # return = 문자열의 마지막 + 해당 문자열의 마지막을 제외한 문자열을 다시 함수의 인자로 사용
                                                # 따라서, reverse_string('abc') = 'c' + reverse_string('ab') =  'c + ('b' + reverse_string('a'))
                                                # = 'c' + ('b' + ('a' + reverse_string(''))) = 'c' + ('b' + ('a' + '')) = 'c' + ('b' + 'a') = 'c' + 'ba' + 'cba'
# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(reverse_string("hello"))  # "olleh"
print(reverse_string("world"))  # "dlrow"
print(reverse_string("python"))  # "nohtyp"
#####################################################
