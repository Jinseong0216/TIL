############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def calculate_number_sum(word):
    number = ['0']                      # 해당 리스트에 찾은 연속된 숫자를 넣고자 함
    s = 0                               # 계산 결과를 담기 위함
    for w in word:
        if w.isdigit():                 # word의 원소가 숫자인 경우 number 리스트에 추가
            number.append(w)
        else:
            s += int(''.join(number))   # word의 원소가 숫자가 아닌 경우, number에 모인 숫자들을 하나로 간주하여 s에 더함
            number = ['0']              # number 리스트 초기화

    if word[-1].isdigit():              # 만약 word의 마지막 원소가 숫자였다면, 마지막으로 발견한 연속된 숫자가 아직 더해지지 않았으므로 체크
        s += int(''.join(number))       # s에 마지막으로 발견한 연속된 숫자를 s에 더함
    
    return s
# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(calculate_number_sum('ab123cd45ef6'))     # 174
print(calculate_number_sum('0a1s2d3f4'))        # 10
print(calculate_number_sum('ssafy10gi2good4560')) # 4572
#####################################################