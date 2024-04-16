'======================== OOP ============================'
# OOP - object-orientated programing 
# OOP - обьектно-ориентированное програмированние (парадигма) 

'-----------------------'
# class Person: 
#     # переменные, которые находятся внутри класса наз. аттрибутами 
#     head = 1  
#     body = 1 

#     def __init__(self, name, age):
#         self.name = name 
#         self.age = age

#     def walk(self): 
#         print(f'{self.name} ходит') 

# obj1 = Person('Tima', 21)
# obj2 = Person('Katana', 35) 
# print(obj1.name, obj1.age, obj1.head, obj1.body)
# print(obj2.name, obj2.age, obj2.head, obj2.body)

# obj1.walk() 
# obj2.walk()
'-------------------------'

' обьекты, экземпляры, instance - конечный продукт, созданный по шаблону класса (он перенимает все аттрибуты и методы класса)'

'------------------------'
# class A: 
#     var1 = 'аттрибут класса' 

#     def __init__(self): 
#         self.var2 = 'аттрибут обьекта'

# print(dir(A)) # класс не видит аттрибуты обьекта 

# obj1 = A() 
# print(dir(obj1)) # обьект видит аттрибуты класса 
'-------------------------'

'self - это ссылка на обьект'
# Что отрабатывает при создании обьекта 
# obj1 = Person('makers', 5)
'__new__ - создает пустой обьект' 
'__init__ - инициализирует этот обьект(создает аттрибуты со значениями внутри пустого обьекта)'

'-------------------------'
# class Calc: 
#     def add(self, a, b):
#         return a + b 
#     def sqrt(self, a): 
#         return a ** 0.5
#     def percent(self, total, _percent): 
#         return (total * _percent) / 100
    
# calc = Calc() 
# print(calc.add(10, 20)) 
# print(calc.sqrt(82)) 
# print(calc.percent(34250, 13))
'---------------------------'

# class Sniper: 
#     health = 100 

#     def __init__(self, name): 
#         self.name = name

#     def shoot(self, sniper): 
#         sniper.health -= 20 
#         print(f'атоковал {self}') 
#         print(f'у {sniper} осталось {sniper.health}')
    
#     def __str__(self): 
#         return self.name

# sniper1 = Sniper('Anonym') 
# sniper2 = Sniper('Tima')

# import random 
# while sniper1.health > 0 and sniper2.health > 0: 
#     choice = random.randint(1,2) 
#     if choice == 1: 
#         sniper1.shoot(sniper2)
#     elif choice == 2:
#         sniper2.shoot(sniper1) 

# if sniper1.health: 
#     print(f'Выиграл снайпер {sniper1}') 
# else: 
#     print(f'Выиграл снайпер {sniper2}') 

# sniper1.shoot(sniper2) 
# sniper2.shoot(sniper1)
# sniper1.shoot(sniper2) 
# sniper2.shoot(sniper1)
# sniper1.shoot(sniper2) 
# sniper2.shoot(sniper1)
'---------------------------'


