number_of_book = 100

def decrease_book(num):
    global number_of_book
    number_of_book -= num
    print(f'남은 책의 수: {number_of_book}')


number_of_people = 0

def increase_user():
    global number_of_people
    number_of_people += 1


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']


def create_user(name, age, addr):
    increase_user()
    user = {'name':name, 'age': age, 'address': addr}
    print(f'{name}님 환영합니다')
    return user


many_user = list(map(create_user, name, age, address))
#print(many_user)

def rental_book(info):
    print(type(info))
    borrow_books = info['age'] // 10
    decrease_book(borrow_books)
    print(f"{info['name']}님이 {borrow_books}권의 책을 대여하였습니다. ")


list(map(rental_book, many_user))
#list(map(rental_book, map(lambda x: {'name':x['name'], 'age':x['age'], 'address': x['address']}, many_user)))
