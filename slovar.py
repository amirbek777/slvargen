import random
import sys

#"это утилита для генерации словарей и надежных парллец для аккаунтов и тд")
chars = '1234567890&$%#&&abcdefjs'
number = input('количество паролей?'+ "\n")
length = input('длина пароля?'+ "\n")
number = int(number)
length = int(length)
for n in range(number):
    password =''
    for i in range(length):
        password += random.choice(chars)
    print(password)
with open("slovarRoot.txt", 'w') as sys.stdout:
    print(password)
