from .base import Person

class Teacher(Person):
    
    def teach(self):
        print(f'{self.name}이 학생을 가르칩니다.')
    
    pass

    
# t1 = Teacher('선생', 50)
# print(t1.name)
# print(t1.eat())
# print(Person.population)
