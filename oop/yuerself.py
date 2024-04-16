# 3) Создайте классы Dog и Cat с одинаковым методом voice.
# Для собак он должен печатать "Гав", для кошек "Мяу".
# Объявите для каждого из классов по экземпляру, для класса Cat экземпляр в
# переменной barsik, а для Dog экземпляр rex.
# Затем, вне класса объявить функцию to_pet(), которая будет принимать животное и
# вызывать у него метод voice().
# Ввод:
# to_pet(barsik)
# to_pet(rex)
# Вывод:
# Мяу
# Гав
# """

class Dog: 
    def voice(self): 
        print('Гав')

class Cat: 
    def voice(self): 
        print('Мяу')


def to_pet(jivotnoe): 
    return jivotnoe.voice()
    
rex = Dog()
barsik = Cat()
to_pet(barsik)
to_pet(rex)

# 1) Создайте класс ToDo, с аттрибутом экземпляра класса, в виде словаря todos = {}.
# У класса должен быть один метод set_deadline, который принимает дату дедлайна (в
# виде "31/12/2021") и возвращает количество дней оставшихся до дедлайна.
# Также, класс ToDo должен наследоваться от четырех миксинов: CreateMixin,
# DeleteMixin, UpdateMixin, ReadMixin:
# в классе CreateMixin определите метод create, который принимет в себя задачу todo и
# ключ key по которому нужно добавить задачу в словарь todos, если ключ уже
# существует верните "Задача под таким ключём уже существует".
# класс DeleteMixin должен содержать метод delete, который удаляет задачу по ключу
# key, который передается как аргумент, и возвращает сообщение 'удалили название
# задачу', где вместо слова название должно быть название задачи.
# класс UpdateMixin должен содержать метод update, который принимает в себя ключ key
# и новое значение new_value и заменяет задачу под данным ключом на новое значение.
# класс ReadMixin должен содержать метод read, который возвращает отсортированный
# список задач.


from datetime import datetime


class CreateMixin:
    def create(self, todo, key):
        if key in self.todos:
            return "Задача под таким ключём уже существует"
        self.todos[key] = todo


class DeleteMixin:
    def delete(self, key):
        if key in self.todos:
            todo = self.todos.pop(key)
            return f'Удалили {todo}'
        else:
            return 'Задача не найдена!'


class UpdateMixin:
    def update(self, key, new_value):
        if key in self.todos:
            self.todos[key] = new_value
        else:
            return 'Задача не найдена!'
    

class ReadMixin:
    def read(self):
        return sorted(self.todos.items())


class ToDo(CreateMixin, UpdateMixin, DeleteMixin, ReadMixin):
    todos = {}

    def set_deadline(self, deadline):
        deadline_date = datetime.strptime(deadline, '%d/%m/%Y')
        current_date = datetime.now()
        days_remainig = (deadline_date - current_date).days
        return days_remainig


todo = ToDo()
print(todo.read())
todo.create('make dinner', 1)
todo.create('make lunch', 2)
todo.create('make bed', 3)
todo.create('make breakfast', 4)
todo.delete(2)
todo.update(1, 'убраться дома')
print(todo.set_deadline("17/09/2024"))

# 2) Напишите класс Person, который будет хранить информацию о пользователе. У
# объекта будут следующие защищенные атрибуты экземпляра класса: имя(name),
# фамилия(last_name), возраст(age), почта (email).
# При инициализации объекта, передавать аргументы классу не нужно, все его атрибуты
# по умолчанию будут равны None и также все они будут приватными.
# Поэтому реализуйте для каждого атрибута методы доступа get и set с использованием
# декораторов property и setter. У вас будут такие методы: name (getter, setter), last_name
# (getter, setter), age (getter, setter) , email (getter, setter)
# Создайте экземпляр john класса Person выедите все его атрибуты, затем измените их
# как показано ниже и после снова выведите на экран.
# Пример:
# john = Person()
# print(john.name) # None
# print(john.last_name) # None
# print(john.age) # None
# print(john.email) # None
# john.name = 'John'
# john.last_name = 'Snow'
# john.age = 30
# john.email = 'johnsnow@gmail.com'
# print(john.name) # John
# print(john.last_name) # Snow
# pclass Person:

class Person:
    def __init__(self):
        self.__name = None
        self.last_name = None
        self.__age = None
        self.__email = None
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def last_name(self):
        return self.__last_name
    
    @last_name.setter
    def last_name(self, value):
        self.__last_name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, value):
        self.__email = value

    
john = Person()
print(john.name)
print(john.last_name)
print(john.age)
print(john.email)

john.name = 'John'
john.last_name = 'Snow'
john.age = 23
john.email = 'johnsnow@gmail.com'

print(john.name)
print(john.last_name)
print(john.age)
print(john.email)
