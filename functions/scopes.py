'========= Области видимости =============='
# LEGB - local enclosed global build-in

'========== Build-in ======================'
# встроенное пространство имен(list, print, dict, len, input)

'============ Global ======================'
# все переменные, которые мы создали внуьри файла 
# чтобы посмотреть все глобальные  переменные, можно использовать функцию globals  
# a = 10 
# b = 'hello'
# print(globals())

'================== enclosed ================='
# # замкнутое пространство имен - это локаальное пространство, у котрого есть внутренее локальное пространство 

# var = 'global' # хранится в глобал. пространстве 

# def func(): 
#     var = 'enclosed' # замкнутое пространство 
#     def inner_func(): 
#         var = 'local' # локальное пространство 
#         print(var) # local 
#     print(var) #enclosed
#     inner_func()
# print(var) # global 
# func()

'=============== Local ==========================='
# локальное пространство имен - это пространство которое находится внутри функции 

# a = 20
# def func(a, b):
#     res = a + b
#     print(res)
#     print(locals())
#     print(globals())

# func(10, 5)

# count = 0
# def count_():
#     global count
#     count+=1
#     print(count)

# count_()
# count_()
# count_()
# count_()


# def count_(num):
#     count = 0
#     def inner_count_():
#         nonlocal count
#         count+=1
#         print(count)
#     for i in range(num):
#         inner_count_()
    
# count_(20)

# def func(): 
#     print('hello world')
#     return func 

# func()()()()()




