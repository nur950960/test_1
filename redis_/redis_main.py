# sudo apt install redis 
# redis-server
# redis-cli

'==========================REDIS========================='
#REMOTE DICTIONARY SERVER - нереляционная БД, для хранения данных, кеша в виде колекций (key-value)
#Redis хранит данные в оперативной памяти, быстрый доступ к данным, но если выключиться свет, то данные исчезнут 


'Способы сохранения данных или восстановления данных'
# 1. RBD(redis database) - бэкап данных из оперативной памяти -> жесткий диск 
# 2. AOF(APPEND ONLY FILE) - сохраняет операции с данными, можно восстановить данные  при помощи AOP

"типа данных в redis"
# String - 
# Json
# List
# Set
# Sorted set
# Stream 
# Hash
# Geospartial 
# Hiperlog
# Bitmap 
# Bitfield

'Практика'
# SET key value - создаем ключ со значением 
# SET key values EX 10 - Создаем временный ключ со значением на 10 сек.

# Get key - смотрим какое значение хранится в ключе key, если такого ключа нет, то выйдет (nil)

# DEL key - мы можем удалить ключ key со значениме

# KEYS * - показывает все ключи в redis 

# SADO group_name(key) value1 value2 value3 - coздаем ключ-набор с нескольким значениями 

# SMEMBERS group_name(key) - показывает значения (участников), которые находятся в group_name(key)

# SREM group_name(key) value - удаляем значение value из group_name(key)
