class Person:
    # class variable 만든다.
    population = 0

    # 생성자 함수
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # 인스턴스 생성 될 때마다 population 1 증가
        Person.increase()   

    # 인스턴스 메서드
    def eat(self):
        print('밥을 먹는다.')

    # 클래스 메서드
    # 데코레이터
    @classmethod
    def increase(cls):
        cls.population += 1

    
    def __str__(self):
        # str 매직메서드의 반환값은
        # print함수로 호출했을때 출력할 값
        return self.name
    
    def __repr__(self):
        return self.name
    


# 인스턴스
# p1 = Person('사람', 10)
# # print(Person.population)
# p2 = Person('인간', 30)
# # print(Person.population)
# print(p1.name, p2.name)
# print(p1.population, p2.population)


# print(p1)   # Person class의 인스턴스 p1이다.
# p1.eat()    # 인스턴스가 호출 할 수 있는 메서드
# p2.eat()    # 모든 Person class의 인스턴스는 eat 메서드 호출 가능.
