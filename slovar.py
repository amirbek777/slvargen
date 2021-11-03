import time 
import random
import sys
import os
import pyfiglet 
from pyfiglet import Figlet

named_tuple = time.localtime() # получить struct_time
time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)

print("Дата и время: ", time_string)

font_text = Figlet(font="slant")
print(font_text.renderText("FireBrut"))
chars = '1234567890'
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
