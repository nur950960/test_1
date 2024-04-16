'================= json =================='
# JavaScript Object Notation - универсальный формат, в котором мы можем хранить данные в типах данных, понятных почти для всех языков програмирования 

import json 
# json_list = "[1,2,3,4,5]"
# python_list = json.loads(json_list)
# print(python_list)
'--------------------------------------'
# json_data = "true"
# python_data = json.loads(json_data)
# print(python_data)
'--------------------------------------'
# json_data = "null"
# python_data = json.loads(json_data)
# print(python_data)
'--------------------------------------'
# with open('test.json', 'r') as file: 
#     python_data = json.load(file)
# print(python_data)

# десериализация - перевод с json строки в python  обьекты 
# loads - метод для десериализация с json строки 
# load - метод для десериализация с json файла 
'-----------------------------------------'


import json 
# python_data = None
# json_data = json.dumps(python_data)
# print(json_data)
'--------------------------------------'
# python_data = [1,2, True, False, None, 'makers']
# with open('test.json', 'w') as file: 
#     json.dump(python_data, file)

# сериализация - перевод python обьектов в json строку 
# dumps - метод для сериализации в json строку 
# dump - метод для сериализации в json файл 
'---------------------------------------'
