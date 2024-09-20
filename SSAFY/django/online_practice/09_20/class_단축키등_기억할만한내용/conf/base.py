class Person:
    # class variable 만들기.
    population = 0 

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.increase() # 인스턴스가 생성될 때마다 population 1씩 증가

    def eat(self):
        print(f'{self.name}이 밥을 먹는다')


    @classmethod
    def increase(cls):
        cls.population += 1

# 인스턴스
# p1 = Person('사람', 10) # Person class의 인스턴스 p1이다.
# p2 = Person('인간', 30) # Person class의 인스턴스 p2이다.
# print(p1.name)
# print(Person.population)
# print(p2.name)
# print(Person.population)
# p1.eat()
# p2.eat()