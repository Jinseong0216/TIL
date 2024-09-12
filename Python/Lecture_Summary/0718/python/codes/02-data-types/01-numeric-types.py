print(2 / 3)
print(5 / 3)

# 부동소수점 문제
a = 3.2 - 3.1
b = 1.2 - 1.1

print(a)
print(b)
print(a == b)

# 부동소수점 해결
from decimal import Decimal

a = Decimal('3.2') - Decimal('3.1')
b = Decimal('1.2') - Decimal('1.1')

print(a)
print(b)
print(a == b)

# 314 ∗ 0.01
number = 314e-2

# 3.14
print(number)

# float
print(type(number))
