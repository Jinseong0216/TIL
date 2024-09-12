class Person:
    def __init__(self, name):
        self.name = name
        print('인스턴스가 생성되었습니다.')

    def greeting(self): 
        print(f'안녕하세요 {self.name}')

person1 = Person('지민')
person1.greeting()