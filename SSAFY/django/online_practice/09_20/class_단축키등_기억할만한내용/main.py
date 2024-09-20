# conf 패키지에 있는 2개의 클래스 모두 가져오기
from conf.student import Student
from conf.teacher import Teacher

s1 = Student('학생', 29)
t1 = Teacher('선생', 30)

t1.teach()
t1.eat()

class Course:
    def __init__(self):
        self.students = []
        self.teacher = []

c1 = Course()
print(c1.students, c1.teacher)
s1 = Student('학생', 29)
t1 = Teacher('선생', 30)
print(s1)

s1.app_for_course(c1)
print(c1.students, c1.teacher)