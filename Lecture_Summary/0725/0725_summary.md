## 07/25(목)

### 09:00 ~ 
- Class 상속

- ParentB.__init__() 으로 할 수도 있으나... 비추

- **Questions** 

    1. class 속성???    

        - class 변수, 메서드, instance, instance변수를 다 포함하는 개념인가???

    2. 위 클래스의 변수를 읽어 올때, class의 정의 단계에서는 불가능 한것인지?
        
        class Dad(Person):
            gene = 'XY'

            def walk(self):
                return '아빠가 걷기'

        class FirstChild:
            def __init__(self, name):
                self.name = name
                self.gene1 = self.gene

        baby1 = FirstChild('아가')
        
        에러 발생

        ```
        class Dad(Person):
            gene = 'XY'

            def walk(self):
                return '아빠가 걷기'


        class FirstChild:
            def __init__(self, name):
                self.name = name

        baby1 = FirstChild('아가')
        print(baby1.gene) 
        ```
        에러 안남

    3. 하위 클래스를 생성 할 때, 
        ```
        class Person:
            def __init__(self, name):
                self.name = name

            def greeting(self):
                return f'안녕, {self.name}'

        class Dad(Person):
            gene = 'XY'

            def walk(self):
                return '아빠가 걷기'


        class FirstChild(Dad, Mom):
            def swim(self):
                return '첫째가 수영'

            def cry(self):
                return '첫째가 응애'
        ```
        
        위의 코드에서 
        `baby1 = FirstChild()`로 아이 클래스를 생성하면 TypeError발생(1 arg missing: name)

        그러나
        `baby1 = FirstChild('아가')`는 잘 작동함.. 여기서 baby1.name은 아가가 됨.
        
        왜?? - 자식 클래스를 만들때, 생성자 메서드에 반드시 부모클래스의 인자를 적어야함!! 그래서 적지 않아도 자동으로 생성!!!!

    4. 하위 클래스를 생성 할 때, 
        ```
        class Person:
            def __init__(self, name):
                self.name = name

            def greeting(self):
                return f'안녕, {self.name}'

        class Dad(Person):
            gene1 = 'XY'

            def walk(self):
                return '아빠가 걷기'

        class Mom(Person):
            gene2 = 'XX'
            def swim(self):
        return '엄마가 수영'


        class FirstChild(Dad, Mom):
            def swim(self):
                return '첫째가 수영'

            def cry(self):
                return '첫째가 응애'
        
        baby1 = FirstChild('아가)
        print(baby1.gene1)
        print(baby2.gene2)
        ```

- `__init__()`을 작성하지 않는 경우!
    - 부모의 `__init__`메서드를 그대로 받아 사용하겠다는 의미임!



- **중요**
    1. `__init__`는 인스턴스 생성 시, 자동으로 실행되는 메서드
    2. `__str__`는 인스턴스가 print 함수로 호출 될 때, 자동으로 실행되는 메서드
    3. 즉, 매직 매서드는 특정 상황에서 자동으로 실행되는 메서드이다.