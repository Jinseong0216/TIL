# add
my_set = {'a', 'b', 'c', 1, 2, 3}

# clear
my_set = {'a', 'b', 'c', 1, 2, 3}

# remove
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.remove(2)
print(my_set)

# pop
for _ in range(10):
    my_set = {'a', 'b', 'c', 1, 2, 3}
    element = my_set.pop()
    print(element)

# discard
my_set = {'a', 'b', 'c', 1, 2, 3}

# update
my_set = {'a', 'b', 'c', 1, 2, 3}

# 집합 메서드
set1 = {0, 1, 2, 3, 4}
set2 = {1, 3, 5, 7, 9}
set3 = {0, 1}

print(set1.difference(set2))
print(set1.intersection(set2))
print(set1.issubset(set2))
print(set3.issubset(set1))
print(set1.issuperset(set2))
print(set1.union(set2))
