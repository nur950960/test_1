'============== Mixins ================'
# Миксины - это классы помошники, которые будут использоваться для наследования. Но от миксинов не создаются объекты 

class FlyMixin:
    def fly(self): 
        print('я могу летать') 

class WalkMixin:
    def walk(self): 
        print('я могу ходить') 

class SwimMixin: 
    def swim(self): 
        print('я могу плавать')

class Human(WalkMixin, SwimMixin):
    name = 'человек' 
    def talk(self): 
        print('я могу говорить')

class Fish(SwimMixin): 
    name = 'рыба'

class Duck(SwimMixin, FlyMixin, WalkMixin): 
    name = 'утка'
    
objects = [Human(), Fish(), Duck()]
attrs = ['fly', 'walk', 'swim', 'talk']
for obj in objects:
    print(obj.name)
    for attr in attrs:
        if hasattr(obj, attr):  
            method = getattr(obj,attr)  
            method()

obj = Human()
setattr(obj, 'name', 'сверхчеловек')
print(obj.name)

# hasattor - это функция, которая принимает объект и название аттрибута. Возвращает True, если у объекта есть такой аттрибут (метод) 
    
# getattr - это функция, которая принмает объект и название аттрибута. Возвращает значения аттрибута 
    
# setattr - это функция, которая принимает объект, название аттрибута и значения аттрибута. Добовляет в объект новый аттрибут или перезаписывает старый аттрибут