'==================ЦИКЛЫ=================='
# циклы - это блок кода, который отрабатывает несколько раз 

''''Итерируемый объект - это какаята последовательность, которую мы можем перебрать. Например: 
[1,2,3] - list 
"Hello world" - str
{"a":1, "b":2} - dict
(1,2,3,4,5,123,True) - Typle' '''

""" Итерация - процесс перебора итерируемого объекта """

# 1. for - это цикл, который работает с итерируемым объектом, цикл заканчивает свою работу, когда он доходит до последнего элемента итерируемого объекта 
# 2. while - это цикл, который работает до тех пор пока условие верное 

'FOR'
# list_ = [1, True, ]


'WHILE'

# count = 0 
# while count < 10: #True #Folse 
#     print(count)
#     count = count + 1 

'================Ключевые слова в циклах============='
# break - это оператор, который остонавливает работу цикла (ломает)
# continue - это оператор, который пропускает итерацию(продолжает с другой итерации)


# range(start, end, step) -генератор последовательности, от start до end (не включительн)

# print(list(range(1, 11)))

# for i in range(0, 21):
#     if i == 10:
#         continue 
#     print(i)

# for i in ['1','2','3', 'hello world']:
#     if i.isdigit():
#         print(int(i))
#         print('Good')
#     elif i.isalpha():
#         print('Error')
#         break 
#     else: 
#         print('Есть символы!')


# count = 0 
# passw = input('Введите пароль: ')
# while True:
#     print(count)
#     if str (count) == passw:
#         print('Вот ваш пароль: ', passw)
#         break 
#     count += 1 #count = count + 1 

# while True: 
#     if count == 0: 
#         continue
#     if count == 1: 
#         break 
#     print(count)
#     count += 1 


#  else: в цикле работает тогда когда условие цикла становится false, если сработал break, то else не работает 



    
