############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장함수 len 함수를 사용하지 않습니다.
def longest_string(str_list):
    max_length = -1                 # 최대 길이를 측정하기 위함
    max_str = None                  # 최대 길이를 가진 문자열을 할당하기 위함
    for char in str_list:
        cnt = 0
        for s in char:              # char 길이 측정
            cnt += 1
        if max_length < cnt:        # char의 길이가 기존의 최대 길이보다 큰지 확인
            max_length = cnt        # 최대 길이 업데이트
            max_str = char          # 최대 길이를 가진 문자열 업데이트
    
    return max_str                  # 최대 길이를 가진(가장 먼저 발견된) 문자열 반환

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 

print(longest_string(["apple", "banana", "cherry", "date"]))  # "banana"
print(longest_string(["cat", "caterpillar", "dog", "elephant"]))  # "caterpillar"
print(longest_string(["a", "ab", "abc", "abcd"]))  # "abcd"

