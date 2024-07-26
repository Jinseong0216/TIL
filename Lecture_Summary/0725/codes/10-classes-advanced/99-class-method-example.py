# 자식 클래스에서 부모 클래스의 클래스 메서드 호출하기


class Animal:
    total_count = 0

    def __init__(self, name):
        self.name = name
        Animal.total_count += 1

    @classmethod
    def get_total_count(cls):
        return f'전체 동물 수: {cls.total_count}'


class Dog(Animal):
    dog_count = 0

    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
        Dog.dog_count += 1

    @classmethod
    def get_dog_info(cls):
        # cls.get_total_count()는 부모 클래스의 클래스 메서드를 호출하여 전체 동물 수를 출력
        return f'{cls.get_total_count()}, 강아지 수: {cls.dog_count}'


class Cat(Animal):
    cat_count = 0

    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
        Cat.cat_count += 1

    @classmethod
    def get_cat_info(cls):
        # cls.get_total_count()는 부모 클래스의 클래스 메서드를 호출하여 전체 동물 수를 출력
        return f'{cls.get_total_count()}, 고양이 수: {cls.cat_count}'


dog1 = Dog('멍멍이', '삽살개')
dog2 = Dog('바둑이', '진돗개')
print(Dog.get_dog_info())  # 출력: 전체 동물 수: 2, 강아지 수: 2


cat1 = Cat('노아', '페르시안')
cat2 = Cat('루비', '코숏')
print(Cat.get_cat_info())  # 출력: 전체 동물 수: 4, 고양이 수: 2
