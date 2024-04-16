
# class Person: 
#     name = "John"

#     _phone_number = "+996 557 55 17 57"
#     __card_number = "9999 9999 9999 9999"

# john = Person()

# print(john.name) 
# print(john._phone_number) 
# print(john._Person__card_number)

'------------------------------'

# class Phone: 
#     def __init__(self, number):
#         self.__number = number

#     @property
#     def number(self): 
#         return self.__number
    
#     @number.setter 
#     def number(self, new_number): 
#         if type(new_number) != str:
#             raise Exception('Введите ввиде текста')
#         if len(new_number) != 13:
#             raise Exception('Некорректный номер') 
#         if not new_number.startswith('+'): 
#             raise Exception('Добавьте символ "+"')
        
#         self.__number = new_number
        
# phone = Phone('+996555555555') 
# print(phone.number) 
# phone.number = '+996555950960'
# print(phone.number)

'---------------------'
# class Person: 
#     def __init__(self, name, phone_number, card_number): 
#         self.name = self.__validate_name(name) 
#         self._phone_number = phone_number
#         self.__card_number = card_number
#     def __validate_name(self, name): 
#         if len(name) < 2:
#             return 'John'
#         else: 
#             return name.title()

# sam = Person("Sam","+996 557 55 17 57","9999 9999 9999 9999" )
# print(sam.name)
# print(sam._phone_number)
# print(sam._Person__card_number)

'---------------------------'
# class Car: 

#     def __init__(self): 
#         self.__speed = 0

#     def set_speed(self, speed): 
#         self.__speed = speed 

#     def show_speed(self): 
#         return self.__speed 

# car1 = Car() 
# print(car1.show_speed()) 
# car1.set_speed(20) 
# print(car1.show_speed()) 

'----------------------------'

# class WalkMixin: 
#     @staticmethod
#     def walk(): 
#         print('я могу ходить')

# class FlyMixin: 
#     @staticmethod
#     def fly(): 
#         print('я могу летать')

# class SwimMixin: 
#     @staticmethod
#     def swim(): 
#         print('я могу плавать')

# class Human(WalkMixin, SwimMixin):
#     ...

# class Fish(SwimMixin):
#     ... 

# class Exocoetidae(FlyMixin, SwimMixin):
#     ...

# class Duck(WalkMixin, FlyMixin, SwimMixin): 
#     ... 
# man = Human()  
# man.swim()
# man.walk()
# fish = Fish()
# fish.swim()
# dragon = Exocoetidae()
# dragon.swim()
# dragon.fly()
# duck = Duck()
# duck.swim()
# duck.fly()
# duck.walk()
'-------------------------'


# class Account:
#     def __init__(self, name, balance, city):
#         self.name = name
#         self.balance = balance
#         self.city = city
#         print('Счет создан')

#     def __str__(self):
#         return f'Hello {self.name} {self.balance} {self.city}'
    
#     def __repr__(self):
#         return f'{self.name} {self.balance}'
    
#     def __del__(self):
#         print('Пока')

# obj_account = Account("Rick", 2013, 'Bishkek')
# print(obj_account)
# print(repr(obj_account)) 
        
'--------------------------------'

# class MyNumber(int): 

#     def __init__(self, value): 
#         self.value = value

#     def __add__(self, num): 
#         return f"Это сложение и результат равен: {self.value + num}"

#     def __sub__(self, num):
#         return f"Это вычитание и результат равен: {self.value - num}"


#     def __mul__(self, num):
#         return f"Это умножение и результат равен: {self.value * num}"

    
#     def __truediv__(self, num):
#         return f"Это деление и результат равен: {self.value / num}"

# obj_int = MyNumber(5)  
# print(obj_int + 5)  
# print(obj_int - 5)  
# print(obj_int * 5)  
# print(obj_int / 5)  

'-------------------------------'

# class OS:
#     def __init__(self, version):
#         self.version = version

# class Windows(OS):
#     def copy(self, text):
#         return f'скопирован текст "{text}" горячими клавишами CTRL + C'
    
# class MacOS(OS):
#     def copy(self, text):
#         return f'скопирован текст "{text}" горячими клавишами COMMAND + C'
    
# class Linux(OS):
#     def copy(self, text):
#         return f'скопирован текст "{text}" горячими клавишами CTRL + SHIFT + C'
    
# win = Windows('10')
# mac = MacOS('Big Sur')
# lin = Linux('Ubuntu')

# print(win.copy('Полиморфизм — одна из основных парадигм ООП'))
# print(mac.copy('Полиморфизм - разное поведение одного и того же метода в разных классах'))
# print(lin.copy('На самом деле одинаковым является только имя метода, его исходный код зависит от класса'))

'-------------------------------------'

# class User:
#     def __init__(self, name, lastname, email):
#         self.name = name
#         self.lastname = lastname
#         self.email = email

#     @staticmethod
#     def validate_email(email):
#         return '@' in email

#     def str(self):
#         if self.validate_email(self.email):
#             return f'{self.name}: {self.email}'

#         return 'email в неправильном формате'

#     @classmethod
#     def create_user(cls, data):
#         list_ = data.split(', ')
#         user = cls(list_[0], list_[1], list_[2])
#         return user


# user1 = User.create_user('John, Snow, john@email.com') 
# user2 = User.create_user('John, Snow, johnemail.com') 

# print(user1)
# print(user2)

'------------------------------------'
# class Circle:
#     color = 'Синий'
#     pi = 3.14 

#     def __init__(self, radius): 
#         self.radius = radius

#     def get_area(self):
#         return self.pi*(self.radius**2)
    
# circle = Circle(radius = 13)
# circle.color = 'желтый'
# print(circle.color)
# print(circle.get_area())

'-----------------------------------'
