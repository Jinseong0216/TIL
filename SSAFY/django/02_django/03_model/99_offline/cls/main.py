# conf 패키지에 있는 2개의 클래스 모두 가져오기
# from conf import students, teacher
from conf.students import Student
from conf.teacher import Teacher

class Course:
    def __init__(self):
        self.students = []
        self.teacher = None

c1 = Course()
print(c1.students, c1.teacher)  # [] None

s1 = Student('학생', 29)
t1 = Teacher('선생', 30)
print(s1)
print(t1)
s1.app_for_course(c1)
print(c1.students, c1.teacher)  # [] None


# c1.teacher = t1
# print(c1.students, c1.teacher)  # [] None

# c1.teacher.eat()
# c1.teacher.teach()
# print(c1.teacher.name)