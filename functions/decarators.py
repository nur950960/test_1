'============== Функция высшего порядка ================='
# функция высшего порядка - это функция которая принимает в аргументы другую функцию, создает внутри себя другую фуекцию, вызывает функцию и возвращает его

# def func1():
#     return 'hi'

# def func2(func_): 
#     print(func_())

# # func2(func1

'============= Декараторы ==============================='
# деораторы - это функция высшего порядка, которая нужна для расширение функционала другой фугкции не изменяя ее (функция обереток)

# def decorator_glushitel(func): 
#     def wrapper(*args, **kwargs):
#         text = func(*args, **kwargs)
#         res = 'тихо ' + text 
#         print(res)
#     return wrapper 


# def gun():
#     return 'стрелять'

# wrapper = decorator_glushitel(gun)
# wrapper() # способ использовать декоратор в ручную

'----------------------------------------------'

# def decorator_glushitel(func): 
#     def wrapper(*args, **kwargs):
#         text = func(*args, **kwargs)
#         res = 'тихо ' + text 
#         print(res)
#     return wrapper 

# @decorator_glushitel
# def gun():
#     return 'стрелять'

# gun() # способ использовать декоратор при поиощи синтаксического сахара

'==========================================================='
# from datetime import datetime

# def decarator(func):
#     def wrapper(): 
#         print('start:', datetime.now())
#         func()
#         print('finish:', datetime.now())
#     return wrapper 

# def hello(): 
#     print('hello world') 

# wrapper = decarator(hello)
# wrapper()
'=========================================================='
# from datetime import datetime

# def func_start_time(func): 
#     def wrapper(*args, **kwargs):
#         print('start:', datetime.now())
#         func(*args, **kwargs)
#     return wrapper

# @func_start_time
# def sum_(a, b): 
#     print(a + b)

# sum_(20, 20)
'==========================================================='
# def decarator(num): 
#     def iner_decarator(func): 
#         def wrapper(*args, **kwargs): 
#             for i in range(num):
#                 func(*args, **kwargs)
#         return wrapper 
#     return iner_decarator

# @decarator(10)
# def hello(): 
#     print('hello world')

# hello()

'==============================================================='
# def call_function(func):
#     def wrapper(*args, **kwargs):
#         print('Вызываю функцию', func.__name__)
#         func(*args, **kwargs)
#         print('Вызов функции', func.__name__, 'прошел успешно')
#     return wrapper


# @call_function
# def first():
#     print("hello world")
#     return "hello world"

# first()
'=============================================='
# from datetime import datetime

# def func_start_time(func):
#     def wrapper(*args, **kwargs):
#         print('Функция запущена ', datetime.now())
#         func(*args, **kwargs)
#     return wrapper

# @func_start_time
# def func():
#     print('Hello world')

# func()
'================================================'
# def make_bold(func):
#     def wrapper(*args, **kwargs):
#         return  '<b>' + func(*args, **kwargs) + '</b>'
#     return wrapper

# def make_italic(func):
#     def wrapper(*args, **kwargs):
#         return '<i>' + func(*args, **kwargs) + '</i>'
#     return wrapper

# def make_underline(func):
#     def wrapper(*args, **kwargs):
#         return '<u>' + func(*args, **kwargs) + '</u>'
#     return wrapper


# @make_bold
# @make_italic
# @make_underline
# def hello():
#     return 'Hello world'
 
# print(hello())
'======================================================='
# import time

# def benchmark(func):
#     def wrapper(*args, **kwargs): 
#         print('Время выполнения: ', time.time())
#         func(*args, **kwargs)
#     return wrapper


# @benchmark 
# def fetch_webpage(): 
#   import requests 
#   webpage = requests.get('https://google.com')  

# fetch_webpage()
'========================================================='
# users = {
#     'user1': 'password1',
#     'user2': 'password2',
#     'user3': 'password3',
# }

# def validate_password(func):
#     def wrapper(username, password):
#         if username in users:
#             if users[username] == password:
#                 return func(username, password)
#             else:
#                 print("Password is invalid")
#         else:
#             print("Username is not defined")
#     return wrapper

# @validate_password
# def login(username, password):
#     print(f'Welcome, {username}')

# login('user1', 'password1')
