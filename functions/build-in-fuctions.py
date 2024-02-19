'================ Встроенные функции ================='
# map, filter, reduce, zip, enumerate 

'ZIP'
# соединяет не сколько пследовательностией (получаем генератор, в котором элементы - tuple) (zip object)

# list_1 = [1,2,3,4]
# list_2 = ['a', 'b', 'c']
# list_3 = [10.5, 20.0, 1.3, 0.5]

# zipped = zip(list_1, list_2, list_3)
# print(zipped) # <zip object at 0x7f1c884e39c0>
# print(list(zipped)) # [(1, 'a', 10.5), (2, 'b', 20.0), (3, 'c', 1.3)]
# print(tuple(zipped)) # ((1, 'a', 10.5), (2, 'b', 20.0), (3, 'c', 1.3))
# print(dict(zipped)) # {1: 'a', 2: 'b', 3: 'c'} (бедет работать тоько с двумя листами в zip())

'ENUMERATE'
# нумерует последовательности (по дефолту с нуля), (тоже возвращает генератор) 
# <enumerate object 0x7kjf4985t78475sjd90>

# enumerated = enumerate('hello world')
# print(enumerated) # <enumerate object at 0x7f50cb37c7c0>
# print(list(enumerated)) # [(0, 'h'), (1, 'e'), (2, 'l'), (3, 'l')......]

# for elem in enumerated:
#     print(elem)

'MAP'
# принимает функцию и последовательность 
# он записывает в новую последовательность в релузьтат функции, применив ее на каждый элемент последовательность 

# <map object 0x7dasgd9asjdh8545jk>

# list_ = ['1', '2', '3', '4']
# mapped = map(int, list_) # <map object at 0x7f5441f40cd0>
# print(list(mapped)) # [1, 2, 3, 4]
'--------------------------------'
# list_2 = ['skk1', '55', 'hsdh222', '662']
# mapped_2 = map(str.isdigit, list_2)
# print(list(mapped_2)) # [False, True, False, True]
'---------------------------------'
# list_ = [12, 34, 1, 2, 6]
# # def pow_(x): 
# #     return x ** 2 

# # print(list(map(pow_, list_))) # [144, 1156, 1, 4, 36]
'---------------------------------'
# print(list(map(lambda x:x ** 2, list_))) # [144, 1156, 1, 4, 36]
'----------------------------------------'
# str_ = 'hello world'
# mapped = map(str.upper, str_)
# print(''.join(list(mapped))) # HELLO WORLD
'---------------------------------------'
# print(''.join(list(map(str.upper, 'hello world')))) # HELLO WORLD
'---------------------------------------'
'FILTER'
# возврвщвет генератор с элементами, прошедшими фильтрацию (какое-то условие), принимает функцию и последовательность

# <filter object 0x7f5441f40cd0>

# list_ = [12, -23, 0, -1, -34, 38]
# filtered = filter(lambda x:x >= 0, list_)
# print(list(filtered)) # [12, 0, 38]
'---------------------------------------'
# users = [
#     {'name':'makers', 'age': 20},
#     {'name':'anonym', 'age': 15},
#     {'name':'sem', 'age':25},
# ]

# users_2 = filter(lambda x:x['age'] >= 18, users)
# print(list(users_2)) # [{'name': 'makers', 'age': 20}, {'name': 'sem', 'age': 25}]
'---------------------------------------'
# users = [
#     {'name':'makers', 'age': 20},
#     {'name':'anonym', 'age': 15},
#     {'name':'sem', 'age':25},
# ]

# users_2 = filter(lambda x:x['name'].startswith('a'), users)
# print(list(users_2))#[{'name': 'anonym', 'age': 15}]
'-----------------------------------------'
'REDUCE'
# принимает функцию и последовательность, но возвращает один элемент (передаваемая функция должна принимать два аргумента )
# # импортируется из functools

# from functools import reduce 

# list_ = [1,23,4,1,5,10]
# res = reduce(lambda x, y: x * y, list_)
# print(res) # 4600
'----------------------------------------'
# users = [
#     {'name':'makers', 'age': 20},
#     {'name':'anonym', 'age': 15},
#     {'name':'sem', 'age':25},
# ]
# from functools import reduce

# def func(x, y): 
#     if x['age'] < y['age']:
#         return x
#     else: 
#         return y

# print(reduce(func, users))
'-----------------------------------------'
# list_ = [1,2,3,4,6,1,9,-1,6,-12]

# from functools import reduce

# def func(x, y): 
#     if x < y:
#         return x
#     else: 
#         return y

# print(reduce(func, list_))
'------------------------------------------'
