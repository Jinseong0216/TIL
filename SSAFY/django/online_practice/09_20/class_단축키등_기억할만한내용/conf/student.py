# 단, 명시성을 지켜주자.
# import base해서 base.Person으로 해도되고


# from base import Person 해도 됨

# 찍어주는 이유 알아보자
# 어떨 때 .base를 쓰는지 알아야함!!

from .base import Person

# 학생 객체 -> 이름, 나이, 먹는다는 행위
class Student(Person):
    def app_for_course(self, course):
        course.students.append(self)
    
    def __str__(self):
        # str 매직메서드의 반환값은
        # print함수로 호출했을때 출력한 값
        return self.name
    
    def __repr__(self):
        return self.name

# s1 = Student('학생', 29)
# print(s1.name)
# s1.eat()
# print(Person.population)