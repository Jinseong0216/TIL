# 1. Positional Arguments
def greet(name, age):
    print(f'안녕하세요, {name}님! {age}살이시군요.')

greet('Harry', 20)
greet(20, 'Harry')
# greet('Harry')


# 2. Default Argument Values
def greet(name, age=20):
    print(f'안녕하세요, {name}님! {age}살이시군요.')

greet('Bob')
greet('Charlie', 40)

# 3. Keyword Arguments
def greet(name, age):
    print(f'안녕하세요, {name}님! {age}살이시군요.')

greet(name='Dave', age=35)
greet(age=35, name='Dave')
# greet(age=35, 'Dave')  # Positional argument cannot appear after keyword arguments

# 4. Arbitrary Argument Lists
def calculate_sum(*args):
    print(args)
    print(type(args))

calculate_sum(1, 100, 5000, 30)


# 5. Arbitrary Keyword Argument Lists
def print_info(**kwargs):
    print(kwargs)

print_info(name='Eve', age=30)


# 인자의 모든 종류를 적용한 예시
def func(pos1, pos2, default_arg='default', *args, **kwargs):
    print('pos1:', pos1)
    print('pos2:', pos2)
    print('default_arg:', default_arg)
    print('args:', args)
    print('kwargs:', kwargs)


func(1, 2, 3, 4, 5, 6, key1='value1', key2='value2')
