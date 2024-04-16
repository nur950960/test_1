'существует три вида методов'

'instance methods - обычные методы, которые принимают первым аргументом self (ссылка на объект)'

# class A: 
#     def instance_method(self): 
#         print('Метод объекта')

# obj = A()
# obj.instance_method()

'class methods - это методы, которые принимают первым аргументом cls (сылка на класс). cls нужно для создания объектов или изменения аттрибутов класса, для создание методов класса нужно задекорировать его classmethod' 

# class B: 
#     @classmethod
#     def class_method(cls): 
#         print('Класс', cls)

# obj = B() 
# obj.class_method()

'-------------------------------'

# class C: 
#     counter = 0 

#     def __init__(self): 
#         self._inc_counter() 

#     def __del__(self): 
#         self._dec_counter()
#         del self

#     @classmethod
#     def _inc_counter(cls): 
#         cls.counter += 1

#     @classmethod
#     def _dec_counter(cls): 
#         cls.counter -= 1

# obj1 = C() # 1 + 0 = 1
# obj2 = C() # 1 + 1 = 2
# del obj2 # 2 - 1 = 1
# obj3 = C() # 1 + 1 = 2
# print(C.counter)

'------------------------'

# class Pizza: 
#     def __init__(self, radius, *ingredients): 
#         self.radius = radius
#         self.ingredients = ingredients 

#     def cook(self): 
#         print(f'Готовится пицца размером: {self.radius*2}')
#         print(f'Ингридиенты: {self.ingredients}')

#     @classmethod
#     def four_cheeze(cls, r):
#         pizza = cls(r, 'Моцарелла', 'Дор блю', 'Чедер', 'Голондский')
#         return pizza 
    
# pizza_1 = Pizza(20, 'Пеперони', 'Моцарелла', 'Курица', 'Салат')
# pizza_2 = Pizza.four_cheeze(20)
# pizza_1.cook()
# pizza_2.cook()

'-------------------------'

'static method - это просто до фуекция внутри класса, который не взаимодействует ни с классом, ни с объектом. Находят эти функции внутри класса, только потому что они полезны внутри, вне класса они бесполезны. Нужно иcпользовать декаратор staticmethod'

# class D: 
#     @staticmethod
#     def hello(str_): 
#         print(str_)

# obj = D() 
# obj.hello('Hi')

'--------------------------'

# class Cylinder: 
#     def __init__(self, diametr, height):
#         self.di = diametr 
#         self.h = height
#         self.area = self.get_area(diametr, height)

#     @staticmethod
#     def get_area(di, h):
#         pi = 3.14
#         circle = pi * di ** 2 / 4
#         side = pi * di * h 
#         area = circle * 2 + side
#         return area 
    
# cylinder = Cylinder(4, 10)
# print(cylinder.area)

# print(Cylinder.get_area(2, 10))


