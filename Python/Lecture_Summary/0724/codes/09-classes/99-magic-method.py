class Circle:
    def __init__(self, r):
        self.r = r

    def __str__(self):
        return f'원의 반지름: {self.r}'
    
    def radi(self):
        return self.r


c1 = Circle(10)
c2 = Circle(1)

print(c1)  # 원의 반지름: 10
print(c2)  # 원의 반지름: 1

print(c1.radi())