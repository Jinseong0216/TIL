# Hello, World!
print('Hello, World!')

# str
print(type('Hello, World!'))

# Escape sequence
print('철수야 \'안녕\'')
print('이 다음은 엔터\n입니다.')


# String Interpolation "f-string"
bugs = 'roaches'
counts = 13
area = 'living room'
print(f'Debugging {bugs} {counts} {area}')


my_str = 'hello'

# 인덱싱
print(my_str[1])  # e

# 슬라이싱
print(my_str[2:4])  # ll
print(my_str[:3])  # hel
print(my_str[3:])  # lo
print(my_str[0:5:2])  # hlo
print(my_str[::-1])  # olleh

# 길이
print(len(my_str))  # 5

# TypeError: 'str' object does not support item assignment
my_str[1] = 'z'
