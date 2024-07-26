# 다중 상속 예시
class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return f'안녕, {self.name}'


class Mom(Person):
    #gene2 = 'XX'
    gene = 'XX'
    def swim(self):
        return '엄마가 수영'


class Dad(Person):
    #gene1 = 'XY'
    gene2 = 'XY'
    def walk(self):
        return '아빠가 걷기'


class FirstChild(Dad, Mom):
    def swim(self):
        return '첫째가 수영'

    def cry(self):
        return '첫째가 응애'
    


baby1 = FirstChild('아가')
print(baby1.name)
#print(baby1.gene1)
#print(baby1.gene2) 
print(baby1.cry())  # 첫째가 응애
print(baby1.swim())  # 첫째가 수영
print(baby1.walk())  # 아빠가 걷기
# print(baby1.gene)  # ??
