'============== SOLID =============='
# SOLID - это аббревиатура для на набора принуипов програмированние, созданых для разработок ПО при помощи ООЯ.

# Принципы SOLID напрвалены на содействие разработки более простого, надежного и обновляемого кода

'1. S(SRP)'
# Single Responsibility Principle 

# 'Принцип единственной обязаности' - это когда у вас один класс отвечает за одну логику (Не нужно создовать один большой класс, который умеет все)
'-----------------------------------'
# # before 
# class ExportCsv:

#     def __init__(self, raw_data): 
#         self.data = self.prepare(raw_data)

#     def prepare(self, raw_data): 
#         result = ''
#         for user in raw_data:
#             new_line = f"{user['name']}, {user['age']}\n"
#             result += new_line 
#         return result
    
#     def write_file(self, filename): 
#         with open(filename, 'w') as f: 
#             f.write(self.data)


# data = [
#     {'name':'Anonym', 'age': 20},
#     {'name':'Makers', 'age':30}
# ]

# obj = ExportCsv(data)
# obj.write_file('out.csv')

'--------------------------------------------'

# after 
# class FormatData:

#     def __init__(self, raw_data):
#         self.raw_data = raw_data

#     def prepare(self): 
#         result = ''
#         for user in self.raw_data:
#             new_line = f"{user['name']}, {user['age']}\n"
#             result += new_line 
#         return result
    
# class FileWriter: 
#     def __init__(self, filename): 
#         self.filename = filename

#     def write_file(self, data): 
#         with open(self.filename, 'w') as f: 
#             f.write(data)

# data = [
#     {'name':'Anonym2', 'age': 20},
#     {'name':'Makers2', 'age':30}
# ]

# formatter = FormatData(data)
# formatted_data = formatter.prepare()
    
# writer = FileWriter('2_out.csv')
# writer.write_file(formatted_data)

'-----------------------------------------'

'2. O(OCP)'
# Open-Closed Principle

# 'Принцип открытости/закрытости' - Програмнные сущности (class, модули, функции) должны быть открыты для расширения, но закрыты для модификации(изменений)

# # before 
# class Discount: 

#     def __init__(self, customer, price): 
#         self.customer = customer
#         self.price = price 
# # если появится новый сигмент, придется добовлять логику на этот сигмент в give_discount() (происходит измениние) 
#     def give_discount(self): 
#         if self.customer == 'vip': 
#             return self.price * 0.6
#         if self.customer == 'premium':
#             return self.price * 0.4
#         if self.customer == 'simple': 
#             return self.price
'--------------------------------------------------'
# # after 
# class Discount: 
#     def __init__(self, customer, price): 
#         self.customer = customer
#         self.price = price 

#     def get_discount(self):
#         return self.price * 0.2
# # если появится новый сигмент, мы просто  создадим новый класс(рассширяем, добовляем)
# class VIPdiscount(Discount):
#     def get_discount(self):
#         return super().get_discount() * 0.2
    
# class PREMIUMdiscount(Discount):
#       def get_discount(self):
#         return super().get_discount() * 0.4

'-----------------------------'
'3. L(LSP)'
# Liskov Subtitution Principle 
#'Принцип подстановки Лисков' 

# Главная идея, стоящая за LSP в том, что для любого класса клиентдолжен иметь возможность использовать любой подкласс базового класса, не замечая разницу между ними 

# Если по простому - родительский класс можно заменить на дочерний не ломая логику работы программы. Т.е наследование должго быть логичным, если в родительском классе есть метод, который есть и в дочерним, то эти методы должны принимать одинаковое количество аргументов 

# class Animal: 
#     def __init__(self, attrs): 
#         self.attrs = attrs 

#     @staticmethod
#     def eat(): 
#         print("Вкусно!")

# class Dog(Animal): 
#     @staticmethod
#     def eat(): 
#         print('Вкусно')

# class Cat(Animal):
#     def eat(food, *bad): 
#         if food in bad: 
#             print('Не вкусно') 
#         else: 
#             print('Вкусно')

# obj_cat = Cat({'name':'barsik', 'age':3})# здесь 
# # если я поменяю дочерний класс Cat на родительский Animal, то код не будет работать - (это неправильно)
# obj_dog = Dog({'name':'rex', 'age':5}) # здесь 
# # если я поменяю дочерний класс Dog на родительский Animal, то код будет работать - (это правильно)
# obj_cat.eat('Курочка', ['сосиски', 'огурцы']) 
# obj_dog.eat()


# # class Car(Animal): 
# #     @staticmethod
# #     def drive():
# #         print('Водить')

# # obj = Car({'name':'barsik', 'age':3})
# # print(obj.drive())
'----------------------------------'

'4. I(ISP)'
# Interface Segregation Principle 
# Принцип разделения интерфейса 

# Создавайте тонкие интерфейсы, которые ориентированы на клиентов. Клиент не должен зависить от интерфейсов, которые они не испоьзуют 

# class Move:
#     def __init__(self, name): 
#         self.name = name 

#     def swim(self): 
#         ... 

#     def fly(self): 
#         ...

#     def walk(self): 
#         ... 

#     def talk(self): 
#         ...

# class Human(Move): 
#     def swim(self): 
#         print(f'Я {self.name}, умею плавать')
#     def walk(self): 
#         print(f'Я {self.name}, умею ходить') 
#     def talk(self):
#         print(f'Я {self.name}, умею говорить')

# class Fish(Move): 
#     def swim(self):
#         print(f'Я {self.name}, умею плавать')
#     def fly(self):
#         print(f'Я {self.name}, умею летать')

# obj_human = Human('Makers')
# obj_human.swim()
# obj_human.walk()
# obj_human.talk()

# obj_fish = Fish('Nemo')
# obj_fish.swim()
# obj_fish.fly()
'--------------------------------'

# # after

# class Move:
#     def __init__(self, name):
#         self.name = name

# class SwimInterface:
#     def swim(self):
#         ...

# class FlyInterface:
#     def fly(self):
#         ...

# class TalkInterface:
#     def talk(self):
#         ...

# class WalkInterface:
#     def walk(self):
#         ...

# class Human(Move, SwimInterface, TalkInterface, WalkInterface):
#     def swim(self):
#         print(f'Я {self.name}, умею плавать')

#     def walk(self):
#         print(f'Я {self.name}, умею ходить')
        
#     def talk(self):
#         print(f'Я {self.name}, умею говорить')

# class Fish(Move, SwimInterface, FlyInterface):
#     def swim(self):
#         print(f'Я {self.name}, умею плавать')

#     def fly(self):
#         print(f'Я {self.name}, умею летать')

# obj_human = Human('Makers')
# obj_human.swim()
# obj_human.walk()
# obj_human.talk()

# obj_fish = Fish('Nemo')
# obj_fish.swim()
# obj_fish.fly()
'---------------------------------'

'5. D(DIP)' 
# Dependecy Inversion Principle 
# Принцип инверсии зависимостей 

# Зависимость должна быть от абстракции, а не от конкретики. Модули верних уровней не должны зависеть от модулей нижних уровней. Классы верхних и нижних уровней должны зависеть от один и тех же абстракций. Абстракция не должна зависеть от деталей. Детали должны зависеть от абстракции 

# before
# import sys
# import time

# class TerminalPrinter: # norm
#     def write(self, msg): 
#         sys.stderr.write(f'{msg}\n')

# class FilePrinter: #norm
#     def write(self, msg): 
#         with open('log,txt', 'a+', encoding='UTF8') as f: 
#             f.write(f'{msg}\n')

# class Logger: # зависит от двух других классов 
#     def __init__(self):
#         self.prefix = time.strftime('%y-%m-%d | %H:%M:%S ', time.localtime())

#     def log_stdder(self, message): # вызывает write для конкретного класса 
#         TerminalPrinter().write(f'{self.prefix}{message}') 

#     def log_file(self, message):  # вызывает write для конкретного класса 
#         FilePrinter().write(f'{self.prefix}{message}') 

# logger = Logger() 
# logger.log_file('Starting thr program...') 
# logger.log_stdder('Error!')
    
'------------------------------'
# after 
import sys
import time

class TerminalPrinter: # norm
    def write(self, msg): 
        sys.stderr.write(f'{msg}\n')

class FilePrinter: #norm
    def write(self, msg): 
        with open('log,txt', 'a+', encoding='UTF8') as f: 
            f.write(f'{msg}\n')

class Logger: 
    def __init__(self): 
        self.format = '%y-%m-%d | %H:%M:%S '

    def log(self, message, cls_): 
        prefix = time.strftime(self.format, time.localtime()) 
        cls_().write(f'{prefix} {message}')

logger = Logger() 
logger.log('Start...', TerminalPrinter)
logger.log('End...', FilePrinter)