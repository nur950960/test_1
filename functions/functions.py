'=============== Функция ====================='
# функция - это именовынный блок кода, который может принимать аргументы и возвращать результат 

# def get_sum(x, y): # x, y - это параметры 
#     result = x + y 
#     return result

# print(get_sum(10, 20)) # 10, 20 - это аргументы 

# def my_sqrt(num1):
#     return pow(num1, 0.5)

# print(my_sqrt(25))

' Функции соблюдают принцип DRY (don"t repeat yourself )'

'================ Аргументы и параметры================'
# параметры - переменные внутри функции, задаются при создании функции 

# агрументы - значения, которые мы передаем при вызове функции 

'================  Виды параметров =================='
# 1. обязательное 
# 2. не обязательное
#     1. с дефолтом (со значением по умолчанию)
#     2. args( все позиционные аргументы)
#     3. kwargs(все лишние именнованные аргументы)

'================== Виды аргументов ====================='
# 1. Позиционная (по позиции)
# 2. Именованные (по названию (парметр = значения) )

'------------------------------------------'
# num : int = 123
# name : str = 'makers'
'========================='
'========================='
# def calc_():
#     try:
#         num1 = float(input('Enter number:'))
#         num2 = float(input('Enter number:'))
#         oper = input('Enter oper:')
#         if oper == '+': 
#             print(num1 + num2)
#         elif oper == '-':
#             print(num1 - num2)
#         elif oper == '/':
#             print(num1 / num2)
#         elif oper == '*':
#             print(num1 * num2)
#         elif oper == '**':
#             print(num1 ** num2)
#         else: 
#             raise KeyError
#     except KeyError:
#         print('не правилная операция!')
#     except ValueError: 
#         print('число, а не символ!')
#     except ZeroDivisionError:
#         print('нельзя делить на ноль!')

# num1 = int(input('Enter number:'))
# num2 = int(input('Enter number:'))
# oper = input('Enter oper:')

# calc_()
'==========================='
'============================'
'========================='
# db = [
#     {'name':'Tima', 'password':hash('123456789')},
#     {'name':'Nick', 'password':hash('205221000')}
# ]

# def in_database(name):
#     for user in db:
#         if name == user['name']:
#             return True
#     return False

# def register(name, password, password2):
#     if in_database(name):
#         raise Exception('Юзер с таким именем уже существует')
#     if password != password2:
#         raise Exception('Пароли не совпадают')
#     user = {'name':name, 'password':hash(password)}
#     db.append(user)
#     return 'Вы успешно зарегестрировались'

# def login(name, password):
#     if not in_database(name):
#         raise Exception('Пользователь не найден!')
#     for user in db:
#         if user['name'] == name:
#             if user['password'] != hash(password):
#                 raise Exception('Пароль не верный!')
            
#     return 'Вы успешно залогинились'

# print(register('katana', '123123123', '123123123'))
# print(db)
# print(login('katana', '123123123'))

'========================================'
'========================================'

'================= Lambda ======================='
# Lambda - анонимная функция, которая записывается в одну строчку 

# def sum_1(x, y):
#     return x + y

# sum_1(10, 29)
# sum_1(1, 5)
# sum_1(20, 1)

# sum_2 = lambda x, y: x + y 
# print(sum_2(10, 5))






    

