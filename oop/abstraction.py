'===================================Absctraction============================'
# Принцип ООП, в котором создается класс-пустышка, где задаются названия аттрибутов и методов, 
# для того чтобы в дочерних классах не забыть их переопределить 

#Шаблон для классов 

# from abc import ABC, abstractmethod

# class Animal(ABC): 
#     @abstractmethod
#     def voice(self):
#         pass 

#     @abstractmethod
#     def move(self):
#         pass 

# class Dog(Animal): 
#     def voice(self): 
#         print('bark')

#     def move(self):
#         print('move')

# class Cat(Animal):
#     def voice(self):
#         print('meow')

#     def move(self): 
#         print('move')


# obj = Dog()
# cat = Cat()


'==========================================Полиморфизм======================================='
# Полиморфизм - это принцип ООП, в котором в разных классах существует одинаково названные методы, но с разной реализацией 

# class Dog:
#     def speak(self): 
#         print('Gav-gav')
# class Cat: 
#     def speak(self): 
#         print('meow')
# class Frog: 
#     def speak(self): 
#         print('kwa')

# objects = [Dog(),Cat(),Frog(), Dog(), Dog(), Frog()]
# for obj in objects:
#     obj.speak()

'==========================================Ассоциация========================================'
# Ассоциация - это принцип ООП, когда два класса связаны друг с другом
"Агрегация - слабая связь"
"Композиция - сильная связь"

class Gun:
    def __init__(self,name) -> None:
        self.name = name
    def shoot(self):
        print('Стрелять')

class Robo_1: 
    def __init__(self, name, gun): 
        self.name = name
        self.gun = Gun('АК')
    
class Robo_2:
    def __init__(self,name,gun):
        self.name =  name
        self.gun = gun
    
robo_1_k = Robo_1('Optimus')
print(robo_1_k)
del robo_1_k #Композиция, оружие удалилось вместе с объектом

gun_for_robo_2 = Gun('glock')
robo_2_a = Robo_2('Optimus',gun_for_robo_2)

robo_3_a = Robo_2('Bee', gun_for_robo_2)
del robo_2_a #Агрегация, оружие не удалилось, так как слабая связь 

'--------------------------------------------------------------------'

class Battery: 
    _power = 100 
    def change(self):
        if self._power <100:
            self._power = 100

class IPhone:
    def __init__(self,color): 
        self.color = color
        self.battert = Battery()
        #Когда мы создаем объект от другого класса внутри класса - композиция

class Nokia:
    def __init__(self, color, battery):
        self.color = color 
        self.battery = battery
        # Когда мы создаем объект вне класса и передаем ее через переменную (агрегация)

iphone = IPhone('black')
del iphone #Композиция, при удалении iphone удаляется battery
battery = Battery()
nokia = Nokia('white', battery)
del nokia  #агрегация, при удалении nokia battery не удаляется. Его можно использовать для других телефонов