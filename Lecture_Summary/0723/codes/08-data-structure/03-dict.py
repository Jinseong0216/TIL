# clear
person = {'name': 'Alice', 'age': 25}
person.clear()
print(person)




# get
person = {'name': 'Alice', 'age': 25}
print(person.get('name'))
print(person.get('country'))
print(person.get('country', 'unknown'))




# keys
person = {'name': 'Alice', 'age': 25}
print(person.keys())
for key in person.keys():
    print(key)




# values
person = {'name': 'Alice', 'age': 25}
print(person.values())
for value in person.values():
    print(value)




# items
person = {'name': 'Alice', 'age': 25}
print(person.items())
for key, value in person.items():
    print(key)
    print(value)





# pop
person = {'name': 'Alice', 'age': 25}
print(person.pop('age'))
print(person)
print(person.pop('country', None))
#print(person.pop('country'))



# setdefault
person = {'name': 'Alice', 'age': 25}
print(person.setdefault('country', 'KOREA'))
print(person)




# update
person = {'name': 'Alice', 'age': 25}
other_person = {'name': 'Jane', 'gender': 'Female'}

person.update(other_person)
print(person)

person.update(age=100, country='KOREA')
print(person)



