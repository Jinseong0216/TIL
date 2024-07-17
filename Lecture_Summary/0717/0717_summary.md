# 07/17(수)

- ### 라이브 강의 (09:00 ~ 10:00)

    - Python 함수 구조상 `return`이 반드시 필요하기 때문에 실제 함수 작성에서
        
        `return`을 정의하지 않을 시, 자동으로 `return None`이 되도록 설계됨.

        ```
        def make_sum(pram1, pram2):
        """이것은 두 수를 받아
        두 수의 합을 반환하는 함수입니다.
        >>> make_sum(1, 2)
            3
        """
        return pram1 + pram2

        result = make_sum(100, 30)
        return_value = print(result) 
        print(return_value)                
        ```

        `결과 값으로 130과 None`이 나옴을 알 수 있음
            
        -  print함수는 return값이 없음

    - 함수의 매개변수(parameter)와 인자(argument)
        
        - 두 대상은 **다른** 대상임

        - 매개변수: 함수를 정의할 때, 함수가 받을 값을 나타내는 변수
            ```
            def add_numbers(x,y):                   # x와 y는 매개변수
                result = x+y
                return result
            ```

        - 인자: 함수를 호출할 때, 실제로 전달되는 값
            ```
            a = 2
            b = 3
            sum_result = add_numbers(a,b)           # a와 b는 인자
            print(sum_result)
            ```

    - 위치인자: 함수 호출 시 인자의 위치에 따라 전달되는 인자

        위치인자는 함수 호출 시 **반드시** 값을 전달해야 함
        ```
        def greet(name, age):
            print(f'안녕하세요, {name}님! {age}살 이시군요.')

        greet('Harry', 20)
        ```

        ```
        >>> 안녕하세요, Harry님! 20살 이시군요.
        ```
        greet('Harry')로 코드를 작성한다면 인자 누락 에러가 나옴

    - 기본 인자 값(Default Argument Values): 함수 정의에서 매개변수에 기본 값을 할당하는 것
    
        함수 호출 시 인자를 전달하지 않으면, 기본 값이 매개변수에 할당됨
        ```
        def greet(name, age=20):
            print(f'안녕하세요, {name}님! {age}살 이시군요.')

        greet('Bob')
        greet('Charlie', 40)
        ```
        
        >>> 안녕하세요, Bob님! 20살 이시군요.

        >>> 안녕하세요, Charlie님! 40살 이시군요.

    - 키워드 인자(Keyword Arguments)

        함수 호출 시 인자의 이름과 값을 전달하는 인자

        매개변수와 인자를 일치시키지 않고, 특정 매개변수에 값을 할당할 수 있음

        인자의 **순서는 중요**하지 않음. 인자의 **이름을 명시하여 전달**

        **주의사항!!!**
        - 키워드 인자는 함수 호출 시, 반드시 위치 인자의 뒤에 위치해야 함!!!!!!!
        
            ```
            def greet(name, age):
                print(f'안녕하세요, {name}님! {age}살 이시군요.')

            greet(name ='Dave', age = 35)
            greet(age = 35, name = 'Dave')
            greet(age = 35, 'Dave')   <<< 에러나는 부분
            ```

    - 임의의 인자 목록
    
        정해지지 않은 개수의 인자를 처리하는 인자

        함수 정의 시 매개변수 앞에 *를 붙여 사용하며, 여러 개의 인자를 **tuple**로 처리
        
        `def main(*args)` 처럼 사용
        
        `def main(*args, params)`: params의 의미가 없음
        
        `def main(params, *args)`: params의 기능을 함

    - 임의의 키워드 인자 목록

        함수 정의 시 매개변수 앞에 \*\*를 붙여 사용, 여러개의 인자를 **dictionary**로 처리
        ```
        def print_info(**kwargs):
            print(kwargs)

        print_info(name ='Eve', age = 30)
        ```
    - **함수 인자 권장 작성순서**

        위치 --> 기본 --> 가변 --> 가변 키워드

        호출 시 인자를 전달하는 과정에서 혼란을 줄일 수 있도록 하기 위함
        ```
        def func(pos1, pos2, default_arg='default', *args, **kwargs):
            print('pos1:', pos1)
            print('pos2:', pos2)
            print('default_arg:', default_arg)
            print('args:', args)
            print('kwargs:', kwargs)


        func(1, 2, 3, 4, 5, 6, key1='value1', key2='value2')        
        ```
        ```
        >>>
        pos1: 1
        pos2: 2
        default_arg: 3
        args: (4, 5, 6)
        kwargs: {'key1': 'value1', 'key2': 'value2'}
        ```
- ### 라이브 강의(10:00 ~ 11:00)
    - 재귀함수의 장점
        1. 복잡한 문제를 간결하고 직관적으로 표현이 가능
        2. 코드가 간결함
        3. 수학적 정의가 재귀적으로 표현되는 경우, 직접적인 구현이 가능
    
    - map과 zip
        ```
        numbers1 = input().split()
        print(numbers1)  # ['1,', '2,', '3']

        numbers2 = list(map(int, input().split()))
        print(numbers2)  # [1, 2, 3]
        ```
        ```
        girls = ['jane', 'ashley']
        boys = ['peter', 'jay']
        pair = zip(girls, boys)

        print(pair)  # <zip object at 0x000001C76DE58700>
        print(list(pair))  # [('jane', 'peter'), ('ashley', 'jay')]    
        ```
        ```
        kr_scores = [10, 20, 30, 50]
        math_scores = [20, 40, 50, 70]
        en_scores = [40, 20, 30, 50]

        for student_scores in zip(kr_scores, math_scores, en_scores):
            print(student_scores)

        """
        (10, 20, 40)
        (20, 40, 20)
        (30, 50, 30)
        (50, 70, 50)
        """    
        ```
        ```
        scores = [
            [10, 20, 30],
            [40, 50, 39],
            [20, 40, 50],
        ]

        for score in zip(*scores):
            print(score)

        """
        (10, 40, 20)
        (20, 50, 40)
        (30, 39, 50)
        """    
        ```
    [이미지 검색 규칙](<img src="https://github-production-user-asset-6210df.s3.amazonaws.com/32388270/249051217-15b4f0c6-7f21-4986-8349-fd8740e49573.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20240717%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240717T013815Z&X-Amz-Expires=300&X-Amz-Signature=4b432f0070fe779f577e70f769ddfddcbdf8ce6482ec52d17573c18de74ead77&X-Amz-SignedHeaders=host&actor_id=175368794&key_id=0&repo_id=329857415" width="128" height="128">)

    - **왜 그런지 생각해 보자**
        ```
        a = 1
        b = 2


        def enclosed():
            a = 10
            c = 3

            def local(c):
                print(a, b, c) # 10 2 500

            local(500)
            print(a, b, c) # 10 2 3


        enclosed()
        print(a, b) # 1 2
        ```

    - **개수가 안 맞는 경우의 unpacking 어떻게 될지 생각**
        ```
        packed_values = 1, 2, 3, 4, 5
        a, b, c, d, e = packed_values
        print(a, b, c, d, e)  # 1 2 3 4 5
        # ab,c = packed_values ...?
        ```

    - paking, unpaking
        ```
        numbers = [1, 2, 3, 4, 5]
        a, *b, c = numbers

        print(a) # 1
        print(b) # [2, 3, 4]
        print(c) # 5
        ```

    - **딕셔너리 언패킹 가능**

        다만, 딕셔너리의 키가 함수의 **인자이름과 일치**해야 함

    - lambda 표현식: **익명 함수**를 만드는 데 사용
    
        1. map과 함께 사용할 때, 아주 유용함
            ```
            numbers = [1, 2, 3, 4, 5]
            def square(x):
                return x**2

            # lambda 미사용
            squared1 = list(map(square, numbers))
            print(squared1)  # [1, 4, 9, 16, 25]

            # lambda 사용
            squared2 = list(map(lambda x: x**2, numbers))
            print(squared2)  # [1, 4, 9, 16, 25]
            ```

        2. 일회성으로 사용 할 때, 보통 lambda 사용함
            ```
            def plus(x,y):
                return x+y

            print(plus(1, 10)) # 11 출력
            print((lambda x, y: x + y)(1, 10)) # 11 출력
            ```
- ### 하늘쌤 요약(11:00 ~)
    - def는 함수를 재사용 하기 위해서임(lambda랑 다름)
    - parameter와 argument차이를 확실히 아는게 좋음
        - parameter는 값이 아직 결정되지 않음
        - parameter는 함수 정의시에 사용
        - argument는 값을 정해서 할당하는 것임
    - 라이브 강의 바탕으로 시험 나오는 듯
    - 함수의 이름은 동사와 명사를 합쳐서(권장)
    - global의 개념은 알고리즘을 다룰 때, 알면 아주 좋음
    - global 변수 변경하는 방법
        ```
        s = 0
        def main():
            global s
            s += 1

        main()
        print(s)
        main()
        print(s)    
        ```
        >>> 1

        >>> 2
    - lambda를 map과 zip에서 활용하면 아주 좋다.

    - 결과는..?
        ```
        A = ['a', 'b', 'c', 'd']
        B = [1, 2, 3]
        print(zip(A, B))
        ```

# 교재 위주로 출제 예정

(꼼꼼히 보기)