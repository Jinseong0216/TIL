# pythonic 하다.
# 10진수로 형변환
print(int('10'))
# 2진수로 변환
print(bin(10))  # 주의. 문자열
# 0b1010    -> 0b 라는 문자열로 2진수를 나타냈음을 표기
print(oct(10))
print(hex(10))

# 16진법 -> 10진법
print(int('F', base=16))
print(int('1010', base=2))

print(bin(8)[2:])   # 4bit로 표기 -> 전처리
print(bin(1)[2:].zfill(4))

for i in range(16):
    print(bin(i)[2:].zfill(4))

# bin_to_hex = {
#     '0000': '0',
#     '0001': '1',
#     '0010': '2',
#     '0011': '3',
#     ...
#     '1111': 'F',
# }
bin_to_hex = {}
for i in range(16):
    print(bin(i)[2:].zfill(4))
    print(hex(i)[2:])
    print(f'16진수 변환 소문자: {i:x}')
    print(f'16진수 변환 대문자: {i:X}')
    print(f'2진수 변환 : {i:04b}')
    bin_to_hex[f'{i:04b}'] = f'{i:X}'
    # bin_to_hex[bin(i)[2:].zfill(4)] = hex(i)[2:]
print(bin_to_hex)
hex_to_bin = {f'{i:X}': f'{i:04b}' for i in range(16)}
print(hex_to_bin)