'==================List================'
# # списки - изменяемый,индексируемый,упорядочный, итерируемый тип данных, предназначенный для хранения любых данных в определенном порядке 
# list1 = [1, 2, 3, 'makers', 'num',[4, 5, 6], True, False, None]
# print(list1[2]) # выйдет 2 
# print(list1[-1]) # выйдет None 
# print(list1[3:-2]) # от num до true  
# print(list1[2][3][2]) 

# string = 'hello'
# res = list(string)
# print(string.split()) #['hello']
# print(res) # ['h','e','l','l','o',]

# list_ = []
# list_ = list()
# list_ = [2] * 10 
# print = (list_)

'==============методы строк=============='
# #append - добавление элементы в конец списка  
# list_ = []
# list_.append(True)
# list_.append('text')
# list_.append(123)
# print(list_) # [True, 'text', 123, ]

# # pop - удоляет элемент из списа по индексу и возвращает удаленный элемент, если не передать индекс в скобки то удалит последний элемент 
# list_ = [1,2,'nur',4,5,6,7,8]
# popped_elem = list_.pop(2)
# print(popped_elem) # удолил 'nur'
# print(list_) #дает текст без 'nur'


# list_ = [12, 'makers', 'nur', 234, True, 0, 1, 2, 3, 4]
# list_.remove(0)
# print(list_)


# #count - метод, который считает кол-во элементов в списке 

# list_ = [0, 12, 'hi', True, False, True, 0, 1, 1, 0]
# count_of_elem = list_.count(1)
# print(count_of_elem) # 4

' --------------------------- '

# #index - возвращает индекс первого вхождения указанного элемента 
 
# list_ - [12, 1, 1, 1, 'hi', None]
# index_ = list_.index('hi')
# print(index_) # 4

#insert - добовляет элемент в список по указаному индексу 

# list_ = [87, 11, 23, 'hi', 5, 1, True, 'world']
# list_.insert(4, 'makers')
# print(list_)

'--------------------------'
# #extend - добовляет элменты списка в другой список 
# list1 = [0, 0, 0]
# list2 = [1, 2, 3]
# list1.extend(list2) #[0, 0, 0, 1, 2, 3]
# print(list1)


#reverse - расстовляет элементы  в обратном порядке

# list_ = [1, 2, 3, 4, None [1,2,3]]
# list_.reverse()
# print(list_) # [[1,2,3], None, 4,3,2,1]

#sort - сортирует список, состоящий из элементов одного типа данных 

# list_ = [23, 1, 24, 23, 123, 0]
# list_.sort()
# print(list_) # [0, 1, 23, 23, 24, 123]

# list_ = ['hi', 'makers', 'hello', 'world']
# list_.sort(key=len, reverse=True)
# print(list_) #'==================List================'
# # списки - изменяемый,индексируемый,упорядочный, итерируемый тип данных, предназначенный для хранения любых данных в определенном порядке 
# list1 = [1, 2, 3, 'makers', 'num',[4, 5, 6], True, False, None]
# print(list1[2]) # выйдет 2 
# print(list1[-1]) # выйдет None 
# print(list1[3:-2]) # от num до true  
# print(list1[2][3][2]) 

# string = 'hello'
# res = list(string)
# print(string.split()) #['hello']
# print(res) # ['h','e','l','l','o',]

# list_ = []
# list_ = list()
# list_ = [2] * 10 
# print = (list_)

'==============методы строк=============='
# #append - добавление элементы в конец списка  
# list_ = []
# list_.append(True)
# list_.append('text')
# list_.append(123)
# print(list_) # [True, 'text', 123, ]

# # pop - удоляет элемент из списа по индексу и возвращает удаленный элемент, если не передать индекс в скобки то удалит последний элемент 
# list_ = [1,2,'nur',4,5,6,7,8]
# popped_elem = list_.pop(2)
# print(popped_elem) # удолил 'nur'
# print(list_) #дает текст без 'nur'


# list_ = [12, 'makers', 'nur', 234, True, 0, 1, 2, 3, 4]
# list_.remove(0)
# print(list_)


#count - метод, который считает кол-во элементов в списке 

# list_ = [0, 12, 'hi', True, False, True, 0, 1, 1, 0]
# count_of_elem = list_.count(1)
# print(count_of_elem) # 4

' --------------------------- '

# #index - возвращает индекс первого вхождения указанного элемента 
 
# list_ - [12, 1, 1, 1, 'hi', None]
# index_ = list_.index('hi')
# print(index_) # 4

'-----------------------------------'
# #insert - добавляет элемент список по указанному индексу
# list_ = [1,2,3,'hi',5,1,True,'world']
# list_.insert(4, 'makers')
# print(list_) # [1, 2, 3, 'hi', 'makers', 5, 1, True, 'world']

'-----------------------------------------'
# #extend - добавляет элементы списка в другой список
# list1 = [0,0,0]
# list2 = ['hi', True,None, 123,12]
# list1.extend(list2) # [0, 0, 0, 'hi', True, None, 123, 12]
# print(list1)

'--------------------------------------'
# #reverse - расставляет элементы в обратном порядке
# list_ = [1,2,3,4, None, [1,2,3]]
# list_.reverse()
# print(list_) # [[1, 2, 3], None, 4, 3, 2, 1]

'-------------------------------------'
# #sort - сортирует список, состоящий из элементов одного типа данных
# list_ = [23, 1, 24, 23, 123, 0]
# list_.sort()
# print(list_) # [0, 1, 23, 23, 24, 123]

# list_ = ['mekers', 'hi', 'asd', 'qwerty']
# list_.sort(key=len, reverse=True)
# print(list_) # ['mekers', 'qwerty', 'asd', 'hi']

'======================Typle================='


# #кортеж - упорядочнный, неизменяеммый, итерируемый тип данных, литералы(,)
# tuple_ = (1,2,3,True,False,None, 'hi' )
# print(dir(typle()))
# #есть только два метода - index и count 

