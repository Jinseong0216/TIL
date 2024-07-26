############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def is_user_data_valid(user_data): # user_data = {id_1: pw_1, id_2: pw_2, ...}
        id, pw = user_data['id'], user_data['password']

        if id and pw: return True
        else: return False

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
user_data1 = {
    'id': '',
    'password': '1q2w3e4r',
}
print(is_user_data_valid(user_data1)) # False 


user_data2 = {
    'id': 'jungssafy',
    'password': '1q2w3e4r',
}
print(is_user_data_valid(user_data2)) # True
#####################################################

user_data3 = {'id': '', 'password': '123'}
print(is_user_data_valid(user_data3))
user_data4 = {'id': 'aab', 'password': ''}
print(is_user_data_valid(user_data4))