'=======================Set==============='
# Множества - это изменяемый, не упорядочный, итерируемый, неиндексируемый тип данных, преднозначенный для хранения уникальных значений.

# Множества могут хранить в себе только не изменяемые типы данных, если же в set использовать tuple, то внутри tuple не должно быть изменяемого типа данных 

# set1 = {1, 5, 2, 3, 4, 'hello', None}
# print(set1)

'==============FIFO / LIFO=================='
# FIFO - first in first out 
# LIFO - last in first out 


# set_  = {1,2,3,4,2}
# print(set_)

'==================Методы set============'
# pop - удоляет случайный элемент из set 
# set2 = {1, 2, 3}
# popped = set2.pop()
# print(popped)
# print(set2)
'---------------------------'
# add - добовляет элемент в set 
# set3 = {1,2,3}
# set3.add(3)
# print(set3) # {1,2,3}
'---------------------------'
# remove - удоляет элемент из set по значению 
# set4 = {1,2,3}
# set4.remove(3)
# print(set4)
'------------------------------'
# difference (-)
# set1 = {1,2,3}
# set2 = {3,4,5}
# print(set1 - set2) # {1,2}
# print(set2 - set1) # {4,5}
# print(set1.difference(set2)) # {1, 2}
# print(set2.difference(set1)) # {4, 5}

# set3 = {5, 6, 7}
# set4 = {6, 8, 9}
# print(set3 - set4) # {5, 7}
# print(set4 - set3) # {8, 9}
'----------------------'
# symmetric_difference
# set1 = {1,2,3}
# set2 = {3,4,5}
# print(set1.symmetric_difference(set2)) # {1, 2, 4, 5}
# print(set1)
'----------------------'
# intersection (&)
# set1 = {1,2,3,4}
# set2 = {3,4,5,6}
# print(set1.intersection(set2)) # {3, 4}
# print(set1 & set2) # {3, 4}
'----------------------'
# union - обьеденяет сеты
# set1 = {1,2,3,4}
# set2 = {4,5,6,7}
# print(set1.union(set2))
'----------------------'
# update 
# set1 = {1,2,3,4}
# set2 = {4,5,6,7}
# set1.update(set2)
# print(set1) # {1, 2, 3, 4, 5, 6, 7}

original = [1,2,3,[4,5,6],[7,8,9]]
import copy 
copiya = copy.copy(original)
deep_copy = copy.deepcopy(original)
original[4][2] = 99 
print(copiya)
print(deep_copy)

list_ = {'a':2, 'b':3, 'c':4}
list_1 = list_.setdefault('d', 5)
print(list_)