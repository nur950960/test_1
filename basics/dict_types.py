'==============Словари==============='
# dict - изменяемый,итерируемый,неупорядочный,неиндексируемый тип данных, для хранения данных в парах(ключ:значение)

# user = {'name':'nur', 'age':17,'nick':'yan'}
# print(user['age']) # 17 
# print(user['nick']) # yan   
# print(user['name']) # nur 

#{ключ: значение, ключ:значение...}
# ключ - не изменяемый тип данных, уникальный(если ключ повторяется, то сохраняется тот, еоторый последний)
#значение - любые: и изменяемый, и неизменяемый тип данных, и неизменяемый тип данных. Могут повторяться 

'=====================Создание==============='
# dict1 = {'a':1, 'b':2}
# dict2 = dict ([('a',1),('b',2)]) 
# dict3 = (['a1','b2'])
# dict4 = {}
# dict4['name'] = 'nur'
# dict4['age'] = 100 
# dict4['nick'] = 'yan'
# print(dict4)
'====================Методы словарей=================='

#get - метод, который возвращает значение по ключу, если такого ключа нет то возвращает дефолтное значение, чаще всего None
# user = {
#     'name':'nick',
#     'age': 100,
#     'tel_num': '+112121223'
# }
# print(user['shfjhs']) # KeyError
# print(user.get('sdhgdsj', 'нет такого ключа')) #нет такого ключа 
# print(user.get('name')) # Nick 
# print(user.get('id')) # None 

# # pop - удаляет пару по ключу и возвращает значение
# dict_ = {'a':1, 'b':2, 'c':3}
# popped_volues = dict_.pop('a')
# print(popped_volues) # 1 
# print(dict_) # {'b':2, 'c':3}
 
# popitem - удоляет последнюю пару и возвращает ее 

# dict_ = {'a':1, 'b':2, 'c':3}
# popped_volues = dict_.popitem()
# print(popped_volues) # ('c',3)

#update - разширяет словарь парами из второго словаря 

# dict1 = {1:'a', 2:'b'}
# dict2 = {3:'c',4:'d'}
# dict1.update(dict2)
# print(dict1) 

# clear - очищает словарь 
# dict_ = {1:1, 2:2, 3:3}
# dict_.clear()
# print(dict_)

# fromkeys - метод, для создание нового словаря, импользуя список ключей  
# dict_ = dict.fromkeys([1,2,3,4,5])
# print(dict_)# {1: None,} и т.д 

# dict2 = dict.fromkeys('abcd', 0)
# print(dict2) # {'a': 0, 'b': 0, 'c': 0, 'd': 0}

#items - метод, который достает [((ключ и значение),...)]
#keys - метод, который возвращает ключи  
#volues - метод, который возвращает значения 

# dict_ = {'a': 1, 'b': 2, 'c': 3 }
# print(dict_.values())
# print(dict_.keys())
# print(dict_.items())

'===============Циклы c dict=============='
# dict_ = {'a':1, 'b':2, 'c':3}

# for i in dict_: 
#     print(i)

# dict_ = {'a':1,'b':2,'c':3}
# dict1 = {}
# for k, v in dict_.items():
#     dict1[v] = k 
#     print(dict1)





