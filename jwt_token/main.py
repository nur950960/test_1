import time 
from jwt_handler import *

user = {'username':'makers', 'id':1}

# получаем токен 
jwt_token = encodeJWT(user) 
print(jwt_token)

# проходит время 
time.sleep(6)

# проверяем истек ли токена 
decoded = decodeJWT(jwt_token['access'])
print(decoded) 

# получение новых токенов 
new_jwt = refreshJWT(jwt_token['refresh']) 
print(new_jwt)
