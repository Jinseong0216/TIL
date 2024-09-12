# find
text = 'banana'
print(text.find('a'))
print(text.find('2'))




# index index는 없으면 ValueError
text = 'banana'
print(text.index('a'))
# print(text.index('2')) 





# isupper
string1 = 'HELLO'
string2 = 'Hello'
print(string1.isupper())
print(string2.isupper())





# islower
string1 = 'HELLO'
string2 = 'Hello'
print(string1.islower())
print(string2.islower())




# isalpha
string1 = 'Hello'
string2 = '123heis9876ssh'
print(string1.isalpha())
print(string2.isalpha())




# replace
text = 'Hello, world!'
new_text = text.replace('world', 'Python') # 전부 다 바꾸는 것
print(new_text)

text = 'Hello, world! world world'
new_text = text.replace('world', 'Python') # 전부 다 바꾸는 것
print(new_text)

text = 'Hello, world! world world'
new_text = text.replace('world', 'Python', 1) # 첫 번째, world만 Python으로 변경
print(new_text)

text = 'Hello, world! world world'
new_text = text.replace('world', 'Python', 2) # 두 번째, world만 Python으로 변경
print(new_text)




# strip
text = '  Hello, world!  '
new_text = text.strip()    # '' 제거
print(new_text)




# split                         # 구분자로 리스트로 변경
text = 'Hello, world!'
words = text.split(',') 
print(words)

text = 'Hello, world!'
words2 = text.split()
print(words2)




# join                          # 구분자로 문자열로 연결
words = ['Hello', 'world!']
new_text = '-'.join(words)
print(new_text)




# capitalize
text = 'heLLo, woRld!'
new_text1 = text.capitalize()   # 제일 앞만 대문자로 바꿔주는 것임 나머지를 소문자로!!
print(new_text1)




# title
text = 'heLLo, woRld!'          # 제목 형식 Bbbbb, Bbbb
new_text2 = text.title()
print(new_text2)




# upper                         # 전부 대문자로
text = 'heLLo, woRld!'          
new_text3 = text.upper()
print(new_text3)




# lower                         # 전부 소문자로
text = 'heLLo, woRld!'          
new_text4 = text.lower()
print(new_text4)




# swapcase                      # 대소 변경
text = 'heLLo, woRld!'          
new_text5 = text.swapcase()
print(new_text5)





# 참고
# isdecimal() : 가장 엄격한 기준을 적용, 오직 일반적인 십진수 숫자(0-9)만 True로 인식
print("isdecimal() 메서드 예시:")
print("'12345'.isdecimal():", '12345'.isdecimal())
print("'123.45'.isdecimal():", '123.45'.isdecimal())
print("'-123'.isdecimal():", '-123'.isdecimal())
print("'Ⅳ'.isdecimal():", 'Ⅳ'.isdecimal())
print("'½'.isdecimal():", '½'.isdecimal())
print("'²'.isdecimal():", '²'.isdecimal())
print()

# isdigit() : 일반 숫자뿐만 아니라 지수 표현(²)도 True로 인식
print("isdigit() 메서드 예시:")
print("'12345'.isdigit():", '12345'.isdigit())
print("'123.45'.isdigit():", '123.45'.isdigit())
print("'-123'.isdigit():", '-123'.isdigit())
print("'Ⅳ'.isdigit():", 'Ⅳ'.isdigit())
print("'½'.isdigit():", '½'.isdigit())
print("'²'.isdigit():", '²'.isdigit())
print()

# isnumeric() : 일반 숫자, 로마 숫자, 분수, 지수 등 다양한 형태의 숫자 표현을 True로 인식
print("isnumeric() 메서드 예시:")
print("'12345'.isnumeric():", '12345'.isnumeric())
print("'123.45'.isnumeric():", '123.45'.isnumeric())
print("'-123'.isnumeric():", '-123'.isnumeric())
print("'Ⅳ'.isnumeric():", 'Ⅳ'.isnumeric())
print("'½'.isnumeric():", '½'.isnumeric())
print("'²'.isnumeric():", '²'.isnumeric())

