'===============Comprehensions============='
# генератор - с помощью которого мы можем создавать последовательности использую цикл for в одну строку 

# елемент - for елемент in последовательность 
# елемент - for елемент in последовательность if фильтр 
# елемент1  - if условие1 else елемент2 for елемент in последовательность 

# compr_ = [i for i in range(6)]
# print(compr_)


# compr_1 = []
# for i in range(10):
#     if i % 2 == 0:
#         compr_1.append(i)
#     else: 
#         compr_1.append('elem')
# print(compr_1)


'создайте новый лист использую старыйю В новом листе должно быть только True значение'
# list_ = [12, None, 'hi', 123, 1, 6, 2, True, 0, False]
# new_list_ = [i for i in list_ if bool(i)]
# print(new_list_)

# new_list_2 = [i if bool(i) else 0 for i in list_]
# print(new_list_2)



# list_ = [12, None, 'hi', 123, 1, 6, 2, True, 0, False]
# new_list_2 = []
# for i in list_:
#     if bool(i):
#         new_list_2.append(i)
#     else: 
#         new_list_2.append(0)
# print(new_list_2)


# list_ = [12, 3, 0, 34, 9, 7]
# new_list_ = ['четное' if i % 2 == 0 else 'нечетное' for i in list_]
# print(new_list_)

# list_ = [1, 'hi', 123, 'hello wolrd', True,'makers', False ]
# new_list_2 = []
# for i in list_: 
#     if type(i) == str:
#         new_list_2.append(i)
# print(new_list_2)

# '============'

# new_list = [i for i in list_ if type(i) ==str]
# print(new_list)

# new_list = [i ** 2 for i in list_ if type(i) == int]
# print(new_list)

'===========Виды comprehension============'
# list comprehension -> []
# dict comprehension -> {:}
# set comprehension -> {}

# comprehension генератор -> ()

'=================DICT COMPREHENSION================='
# {1:1, 2:4, 3:9, 4:16}
# dict_ = {i:i**2 for i in range(1,5)}
# print(dict_)

# dict_ = {"a":1, "b":2, "c":3}
# new_dict_ = {v:k for k,v  in dict_.items()} 
# print(new_dict_)
# '=================='
# new_dict_2 = {v**2:v for v in dict_.values()}
# print(new_dict_2)

'SET_COMPREHENSION'
# set_ = {i for i in range(11) if i % 2 == 0}
# print(set_)

# set_1 = {12, 34, 1, 'hi', 'Hello', 'hello', 123, None }
# set_2 = {i.upper() for i in set_1 if type(i)==str}
# print(set_2)

'===================== Вложенные COMPREHENSION ==========================='
# создайте словарь, где ключами будут числа от 1 до 5, а значениями - списки с числами от 1 этого числа 

# dict_ = {}
# for i in range(1,6):
#     key = i 
#     values = [j for j in range(1, i+1)]
#     dict_[key] = values
# print(dict_)

# dict_ = { i: [j for j in range(1, i+1)] for i in range(1, 6)}
# print(dict_) 
'--------------------------------'
# list_ = [x**2 if x % 2 == 0 else x for x in range(1, 11)]
# print(list_)
'--------------------------------'
# list_ = [True if i % 2 == 0 else False for i in range(1, 11)]
# print(list_)
'-------------------------------'
# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ] 
# new_list = ['shorter' if len(i) <= 4 else 'longer' for i in list_name]
# print(new_list)
'-------------------------------'
# dict_ = {k : k * k for k in range(1, 11)}
# print(dict_)
'-------------------------------'
# n = int(input('Введите число от 1 до 10: '))
# dict_ = {key % n % 2 == 0 : key ** 3 for key in range(1, 501)}
# print(dict_)