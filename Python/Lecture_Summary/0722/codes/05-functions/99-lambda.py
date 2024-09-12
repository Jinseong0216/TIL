def addition(x, y):
    return x + y


result = addition(3, 5)
print(result)  # 8


# lambda 표현식으로 작성한 addition 함수
lambda x, y: x + y


# with map 함수
numbers = [1, 2, 3, 4, 5]


def square(x):
    return x**2


# lambda 미사용
squared1 = list(map(square, numbers))
print(squared1)  # [1, 4, 9, 16, 25]

# lambda 사용
squared2 = list(map(lambda x: x**2, numbers))
print(squared2)  # [1, 4, 9, 16, 25]
