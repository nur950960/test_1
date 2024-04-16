'========== Encapsulation ============='
# инкапсуляция - это принцип ООП, у которого есть 2 трактовки 
# 1. сбор всех данных, аттрибутов, методов в одну "капсулу"(class) 
# 2. сокрытие данных, есть 3 уровня скрытия данных 

'Виды доступа к аттрибутам'
# 1. public (публиичный) 
# 2. protected (защищенный) - с одним underscore в начале (_name, _fly) 
# 3. private (приватный) - c двумя underscore (__name, __fly)

# class A: 
#     attr = 'публичный' 
#     _attr2 = 'защищенный' 
#     __attr3 = 'приватный'

# print(A.attr) 
# print(A._attr2)
# # print(A.__attr3) # не найдет, питон добовляет в начало аттрибута underscore и название класса
# print(A._A__attr3)

# # print(A.__dict__)

'============== Getters/setters =============='
# # это функции, для работы с приватными, защищенными и публичными аттрибутами. При помощи этих функций можно получать и менять значение аттрибутов 

# class Person: 
#     def __init__(self, name, age): 
#         self.name = name 
#         self.__age = age
    
#     def get_age(self): 
#         return self.__age 
    
#     def set_age(self, new_age): 
#         if new_age > 0: 
#             self.__age = new_age
#         else: 
#             raise Exception('Возвраст не может быть мменьше 0') 
        
# obj = Person('Anonym', 30) 
# print(obj.get_age()) 
# obj.set_age(50)
# print(obj.get_age())
'---------------------------------------------------------'
class Person:
    def __init__(self, name, age): 
        self.name = name
        self.__age = age

    @property
    def age(self): 
        return self.__age
    
    @age.getter
    def age(self): 
        return self.__age 
    
    @age.setter 
    def age(self, new_age): 
        if type(new_age) != int:
            raise Exception('Введите возраст как число') 
        if new_age > 0: 
            self.__age = new_age
        else: 
            raise Exception('Введите число больше 0') 

obj = Person('Anonym', 30)
print(obj.age) 
obj.age = 50
print(obj.age) 

'@property - это декаратор, который позволяет обращаться к методам как к аттрибутам'

'@name.setter - это декаратор, который позволяет менять значение защищенного аттрибута'

'@name.getter - это декаратор, который позволяет получать значение защищенного аттрибута'

