'РЕЖИМЫ'
#r+
#w+
#a+

"r+ - ОТкрывает файл в режиме чтения + в режиме append(дозаписи)"
# with open('test1.txt', 'r+') as file:
#     print(file.read())
#     file.write('py33')
#     file.seek(0)
#     print(file.read())

"w+ - открывает файл в режиме записи + read(чтения)"

# with open('test1.txt', 'w+') as file: 
#     file.write('Jacob')
#     file.seek(0)
#     text = file.read()
#     print(text)

"a+ - открывает файл в режиме дозаписи + в режиме read(чтения)"

# with open('test1.txt', 'a+') as file: 
#     file.write('makers\n')
#     print(file.read())
#     file.seek(0)
#     file.write('hello\n')
#     file.seek(0)
#     print(file.read())

'============== CSV ==================='

# csv - формат файла 
 
# import csv

# with open('data.csv') as file: 
#     data = csv.reader(file)
#     colm = next(data)
#     print('поле: ', colm)
#     for product in data:
#         print(product)
'==================================================================================================='
# def read_last(lines:int, filename:str):
#     with open(filename, 'r') as file:
#         data = file.readlines() # List[str]
#     data.reverse()
#     if lines >= len(data):
#         for line in data:
#             print(line.replace('\n',''))
#     else:
#         count = 1
#         for line in data:
#             print(line.replace('\n',''))
#             if lines == count:
#                 break
#             count += 1

# read_last(20, 'test1.txt')
'-----------------------------------------'
