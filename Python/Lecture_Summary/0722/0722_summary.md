## 07/22(월) 
[gitlab 파이썬 공통 주소](https://lab.ssafy.com/s12/python/python)  
코딩 중 error 발생 시, 마지막 줄 & 마지막 줄의 윗 줄 정도만 봐도 됨.

### 09:00 ~ 10:00
- 자료구조
    단순, 선형, 비선형, 파일

    - 단순 구조    
        - 정수, 실수, 문자, 문자열

    - 선형 구조
        - 순차 리스트

        - 연결 리스트    
            1. 단순 연결 리스트
            2. 이중 연결 리스트
            3. 원형 연결 리스트
        
        - 스택

        - 큐

        - 덱

    - 비선형 구조    
        - 트리    
            1. 일반 트리
            2. 이진 트리
        
        - 그래프
            1. 방향 그래프
            2. 무방향 그래프

    - 파일 구조
        - 순차 파일

        - 색인 파일

        - 직접 파일

- **method**: 객체에 속한 함수    
    (class 내부에 정의되는 함수)    
    (객체의 상태를 조작하거나 동작을 수행)

    method는 어딘가에 속해 있는 함수

    - method 호출 방법
        객체.함수이름()    
        (객체에 속한, 함수를 불러오시오)    
        이때, 위치한 함수를 method라 함.

        ``` 
        # Example 1
        
        class ABC:
            def method_abd(self):
            print("I am in method_abc of ABC class.")
        
        class_ref = ABC()
        class_ref.method_abd()
        ```

         ```
         # Example 2
         
         'hello'.capitalized()
         ```

         **위 두 예시의 차이를 모르겠음**

- 문자열 조회/탐색 및 검증 메서드 (is 함수들은 반환 값이 boolean)    
    1. `s.find()`

    2. `s.index()`

    3. `s.isupper()`

    4. `s.islower()`

    5. `s.isalpha()`
        - 알파벳 문자 여부

        - 단순 알파벳이 아닌, 유니코드 상 Letter (한국어도 포함)

- 문자열 조작 메서드(새 문자열 반환)    
    왜? 새 문자열을 반환 하는가?    
    **문자열은 불변**이므로

    ( [] <-- 안의 내용은 넣어도 되고 안넣어도 되는 선택 인자임)    
    1. **`s.replace(old, new[count,]`)**

    2. **`s.strip([chars])`**

    3. **`s.split(sep=None, maxsplit = -1)`**

    4. **`'separator'.join(iterable)`**

    5. `s.capitalize()`
        -  제일 앞만 대문자로 바꿔주는 것임

    6. `s.title()`

- 메서드는 이어서 사용이 가능하다.( chainning 가능, 예외가 존재 하긴 함)
    1. 반환 값이 존재하고
    2. 메서드와 반환 값의 타입이 맞을 때

### 10:00 ~ 11:00

- 리스트 값 추가 삭제 메서드
    1. `L.append(x)` 
        - 마지막 항목에 x 추가
    
    2. `L.extend(x)`
        - 리스트에 반복 가능한 객체의 모든 항목을 추가
    
    3. **`L.insert(i, x)`** 
        - 리스트에 지정한 index i 위치에 x를 삽입

    4. **`L.remove(x)`**
        - 리스트에서 첫 번째로 일치하는 항목을 삭제

    5. `L.pop(i)`
        - 리스트에서 지정한 인덱스의 항목을 제거하고 반환   
        - i를 작성하지 않으면 마지막 항목 제거하고 반환

    6. `L.clear()`
        - 리스트의 모든 항목을 삭제
        - return 값이 []이 됨.

- 리스트 탐색 및 정렬 메서드
    1. `L.index(x)`
        - 리스트에서 첫 번째로 일치하는 x의 인덱스 반환
        - 없으면 에러
    2. `L.count(x)`
        - 리스트에서 항목 x의 개수를 반환
    3. `L.reverse()`
        - 리스트를 역순으로 변경 (정렬 X)
    4. `L.sort()`
        - 리스트를 오름차순으로 정렬

- 복사
    1. 파이썬에서는 데이터의 분류에 따라 복사가 달라짐
    2. **변경 가능한 데이터 타입**과 **변경 불가능한 데이터 타입**을 다르게 다룸   

    - 복사의 유형
        1. 할당
        2. 얕은 복사
        3. 깊은 복사
    
- 할당(주소가 복사 된다는 느낌으로 복사 유형에 들어가는 듯)

    ```
    a = [1, 2, 3, 4]
    b = a
    b[0] = 100

    print(a)
    print(b)

    >>> 
    [100, 2, 3, 4]
    [100, 2, 3, 4]
    ```

    a와 b가 같은 대상을 가리킴. 그러나, 이 경우 복사가 아닌 **할당**임

    ```
    a = 20
    b = a
    b = 10

    print(a)
    print(b)    
    
    >>>
    10
    20
    ```
    불변 데이터 타입은 재할당 되어 값이 변경 됨.

    할당 연산자(=)를 통한 복사는 **객체 참조(주소 값)를 복사**

- 얕은 복사
    슬라이싱으로 생성된 객체는 원본 객체와 독립적으로 존재

    ```
    a = [1, 2, 3]
    b = a[:]

    b[0] = 100
    print(a)
    print(b)

    >>>
    [1, 2, 3]
    [100, 2, 3]
    ```

    대상.copy()를 통해서도 얕은 복사가 가능함

    ```
    a = [1, 2, 3]
    c = a.copy()

    c[0] = 999
    print(a)
    print(c)

    >>>
    [1, 2, 3]
    [999, 2, 3]
    ```

    **얕은 복사의 한계**
    2차원 리스트와 같이, 변경 가능한 객체 안에 변경 가능한 객체가 존재하는 경우

    파이썬 튜터를 통해서 보는 것 추천
    ```
    a = [1, 2, [3, 4, 5]]
    b = a[:]

    b[0] = 999
    b[2][1] = 100
    print(a)
    print(b)
    
    >>>
    [1, 2, [3, 100, 5]]     # a
    [999, 2, [3, 100, 5]]   # b
    ```
    a와 b의 주소는 다르지만, 내부 객체의 주소는 같기 때문.

    이런 문제를 해결하기 위해서 copy라는 내장 module이 필요함

- 깊은 복사(deepcopy를 하는 방법은 아래의 module 사용 밖에 없음)

    파이썬 튜터를 통해서 보는 것 추천
    ```
    import copy
    a = [1, 2, [3, 4, 5]]
    b = copy.deepcopy(a)

    b[0] = 999
    b[2][1] = 100
    print(a)
    print(b)

    >>>
    [1, 2, [3, 4, 5]]       # a
    [999, 2, [3, 100, 5]]   # b
    ```


- 문자열에 포함 된 문자들의 유형을 판별하는 메서드
    
    (1이 가장 엄격, ..., 3이 가장 널널 )

    (정확하게 포함 관계임)

    **isdecimal() $\subset$ isdigit() $\subset$ isnumeric()** 
    1. isdecimal()
        - 문자열이 전부 0~9로 이루어져 있어야만 True

    2. isdigit()
        - 유니코드 숫자도 인식( 유니코드 숫자 뭔지 보면 됨)
    3. isnumeric()
        - 분수, 지수, 루트 기호도 숫자로 인식

    ```
    # 참고
    # isdecimal() : 가장 엄격한 기준을 적용, 오직 일반적인 십진수 숫자(0-9)만 True로 인식
    print("isdecimal() 메서드 예시:")
    print("'12345'.isdecimal():", '12345'.isdecimal())
    print("'123.45'.isdecimal():", '123.45'.isdecimal())
    print("'-123'.isdecimal():", '-123'.isdecimal())
    print("'Ⅳ'.isdecimal():", 'Ⅳ'.isdecimal())
    print("'½'.isdecimal():", '½'.isdecimal())
    print("'²'.isdecimal():", '²'.isdecimal())
    print()

    # isdigit() : 일반 숫자뿐만 아니라 지수 표현(²)도 True로 인식
    print("isdigit() 메서드 예시:")
    print("'12345'.isdigit():", '12345'.isdigit())
    print("'123.45'.isdigit():", '123.45'.isdigit())
    print("'-123'.isdigit():", '-123'.isdigit())
    print("'Ⅳ'.isdigit():", 'Ⅳ'.isdigit())
    print("'½'.isdigit():", '½'.isdigit())
    print("'²'.isdigit():", '²'.isdigit())
    print()

    # isnumeric() : 일반 숫자, 로마 숫자, 분수, 지수 등 다양한 형태의 숫자 표현을 True로 인식
    print("isnumeric() 메서드 예시:")
    print("'12345'.isnumeric():", '12345'.isnumeric())
    print("'123.45'.isnumeric():", '123.45'.isnumeric())
    print("'-123'.isnumeric():", '-123'.isnumeric())
    print("'Ⅳ'.isnumeric():", 'Ⅳ'.isnumeric())
    print("'½'.isnumeric():", '½'.isnumeric())
    print("'²'.isnumeric():", '²'.isnumeric())
    ```

    
    - '123.45', '-123'은 모든 경우 False임
        1. 소숫점
        2. \- 부호
    
***
시퀀스 데이터 구조 공부해야할듯;
- **https://docs.python.org/3.9/tutorial/datastructures.html#data-structures 보고 자료구조 공부**
***     

### 11:00 ~ (SKY 요약)
- 각 함수의 기능 시험에 나오는듯?

- 메서드: 클래스에 속한 함수임
    1. **클래스 . 함수이름()**을 통해서 사용 가능
        그 결과, sky1.insert()와 sky2.insert()가 달라짐.
    2. **데이터 타입 객체 . 메서드()**또한 가능. (왜..?)
    
- 데이터 구조 활용
    1. 문자열, 리스트, 딕셔너리 등 각 데이터 구조의 **메서드**를 호출하여 다양한 기능을 활용하기

- SWEA등에서 .rstrip() 사용하면 많이 편한 듯.

- .split()의 경우 인자를 넣지 않으면 공백을 기준으로 나눠줌
    1. 기본 인자가 ' ' 인듯?

- 메서드를 이어서 사용하는 것 편함. (cascading)
```
text = 'heLLo, woRld!'
new_text = text.swapcase().replace('l', 'z')

print(new_text)

>>>
HEzzO, WOrL
```

***
# 싹 다 외워야 함(월말 평가 예상)

- 예시 코드를 만들어 낼 수 있을 정도.

- 특이사항들까지 전부.

1. L.append(x)가 나왔을 때 설명 바로 적을 수 있을 정도(주관식)
2. 설명이 나왔을 때, L.append(x)
3. 예시 코드 만들어 내기
4. 코드로 설명 가능 해야함.

**Ex**
- .pop의 경우 
    1. 뽑은 원소가 return 됨
    2. 리스트는 변경 됨

```
L = [1,2,3,4,5]

item1 = L.pop()
item2 = L.pop(0)

print(item1)
print(item2)
print(L)

>>>
5
1
[2,3,4]
```
...
수준으로 시험 낼 것

- 리스트 값 추가 삭제 메서드
    1. `L.append(x)` 
        - 마지막 항목에 x 추가
    
    2. `L.extend(x)`
        - 리스트에 반복 가능한 객체의 모든 항목을 추가
    
    3. **`L.insert(i, x)`** 
        - 리스트에 지정한 index i 위치에 x를 삽입

    4. **`L.remove(x)`**
        - 리스트에서 첫 번째로 일치하는 항목을 삭제

    5. `L.pop(i)`
        - 리스트에서 지정한 인덱스의 항목을 제거하고 반환   
        - i를 작성하지 않으면 마지막 항목 제거하고 반환

    6. `L.clear()`
        - 리스트의 모든 항목을 삭제
        - return 값이 []이 됨.
***






***
**고려해 볼만한 내용**
1. 금일 실습 내용 중, reversed() 내장 함수를 사용해야 하는 문제가 존재
    - 서칭 해보니, 역방향 반복을 돌리는 경우 reversed() 내장 함수를 사용 하는 것이 자원 소모를 많이 줄여준다 함.
    - reversed()는 반복자 타입을 반환해줌.

2. 시험 공부시에, 파이썬 공식문서 들어가서 코드 전부 작성해 보는 것 권고!!
***     

### 14:00 ~ 