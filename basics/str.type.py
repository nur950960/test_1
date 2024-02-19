'===============String============='
#строки - неизменяемый тип данных,который предназначен для хранения текста, заключенного в одинарные либо двойные кавычки


string4 = "don't"# внутри двойной кавычки все одинарные - просто символы 
string5 = '''
много строчный текст в одинарных кавычках, тут можно ставвить 'любые' кавычки 
'''
string6 = 'hello' + 'word'
print(string6)

string7 = 'A' * 8 
print(string7)

'============экранизация строк============'
'\n' # переносит текст на новую строку 
print ('hello\nword')
#hello 
#world 

'\t'# табуляция 
print ('hello\tworld')
#hello    world 

'str1\'' # отображает кавычку '
print('str1')

str2 = "dont\"t"
print(str2)

str3 = 'символ - \\'
print(str3)

'\v' # перенос на новую строку со смещением в право на длину предыдущей строки 
print('hello\vworld\vmakers\vbootcamp')

'\r' # перенос каретки на начло строки
print('makers bootcamp\rHi') 
#Hikers bootcamp 

'=====================форматирование строк============'
#1
title = 'iphone14'
price = 150 
format_1 = 'мой телефон', title, 'стоит', price, 'долларов' 
format_2 = f'мой телефон {title}, стоит {price} доллоров'
print(format_2)

#2 
string = 'название: {} цена: {}$'
print(string.format('iphone', 150))

#3
string = 'название: %s цена:%s'
print(string % ('iphone', 150))

'==============методы строк============'
# методы - это функции которые относятся к определенному классу, к ним можно общаться через точку 

print(string.upper()) # makers -> MAKERS
price(string.lower()) # MAKERS -> makers
price(string.swapcase()) # MaKErS -> mAkeRs

print(dir(str))
      
string = 'hello world'


print(string.title()) #hello world -> Hello World

print(string.capitalize()) # hello world -> Hello world 

print(string.centre(11)) # '    hello    '
 

print(string.count('h')) #hello world -> 1
 
print(string.startswith('a')) #false 
print(string.startswith('h')) #true
print(string.startswith('H')) # fasle 

print(string.endswith('d')) #false 
print(string.endswith('lo')) #true 


string = 'makers'
print(string.islower()) # makers -> True 
#print(string.isupper()) #MAKERS -> True 


# print = '123456'
# print(string.isdigit()) # true проверка на цифры в тексте 
# print(string.isalpha()) # False - проверка на буквы в тексте
# print(string.isalnum()) # true - проверка на то что является ли строка с числами или с буквами или все вместе,НО НЕ СИМВОЛЫ


string = 'hello world makers bootcamp'
print(string.split()) - #разделает слова по кавычкам 



'==================================================================================================================='
'==================================================================================================================='

'======================раздел индекса================'

#индекс - порядковый номер элемента в последовательности(символа в строке), (индексация начинается с 0)

'h e l l o w o r l d '
#0 1 2 3 4 5 6 7 8 9 10 
#                -3 -2 -1

string = 'hello world'
print(string[0]) # 'h'
print(string[7]) # 'o'
print(string[10]) # 'd'
print(string[-1]) # 'd'

#срезы - подстрока (часть строки )
#string[start:end(не включительно):step]
string = 'hello world'
print(string[3:5]) #'lo wo'
print(string[6:]) # world
print(string[:5]) # 'hello'

print(string[::-1]) # dlrow olleh 
print(string[::2]) #hlowrd
print(string[::3]) # hlwl\


string = ' hello'
string = string.upper() # hello -> HELLO


