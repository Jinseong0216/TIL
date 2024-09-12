# 할당
a = [1, 2, 3, 4]
b = a
b[0] = 100

print(a)
print(b)

a = 20
b = a
b = 10

print(a)
print(b)




# 얕은 복사
a = [1,2,3]
b = a[:]

b[0] = 100
c = a.copy()
c[0] = 999
print(a)
print(b)
print(c)


# 얕은 복사의 한계
a = [1, 2, [3, 4, 5]]
b = a[:]

b[0] = 999
b[2][1] = 100
print(a)
print(b)




# 깊은 복사
import copy
a = [1, 2, [3, 4, 5]]
b = copy.deepcopy(a)

b[0] = 999
b[2][1] = 100
print(a)
print(b)