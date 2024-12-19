import random
lon = int(input("¿De que longitud será tu contraseña?"))
password = ''
for i in range(lon):
    ce = random.choice(".,;:?!'()[]{}-0123456789abcdefghijqlmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    password = password + ce
print("la contraseña es:" + password)
