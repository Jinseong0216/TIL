from decimal import Decimal

# 원주율
3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
# 반지름
15

pi = '3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679'
radius = '15'

perimeter = 2*Decimal(pi)*Decimal(radius)
perimeter = str(perimeter)

area = Decimal(pi)*Decimal(radius)**2
area = str(area)

print(f'원주율 : {pi[:17]}')
print(f'반지름 : {radius}')
print(f'원의 둘레 : {perimeter[:17]}')
print(f'원의 넓이 : {area[:17]}')