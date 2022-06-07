#!/bin/python3
from cairo import Status


print("Введите первое число")
number1=int(input())
print("Введите второе число")
number2=int(input())
print("Введите третье число")
number3=int(input())
#Task1  
status=True
while number1 !=0 and number2 !=0 and number3 !=0 and status==True:
    print('Нет нулевых значений!!!')
    status=False
#Task2    
while number1 > 0 and status==True:
    print("Первое ненулевое значение= ", number1)
    status = False
while number2 > 0 and status==True:
    print("Первое ненулевое значение= ", number2)
    status = False
while number3 > 0 and status==True:
    print("Первое ненулевое значение= ", number3)
    status = False
while number1 == 0 and number2 == 0 and number3 == 0 and status==True:
    print("Введены все нули!")
    status = False    
#Task3
if number1 > (number2 + number3):
    print('a - b - c=', number1 - number2 - number3)
#Task4      
if number1 < (number2 + number3):
    print('b + c - a=', number2 + number3 - number1)
#Task5    
if number1 > 50 and (number2 > number1 or number3 > number1):
    print('Вася')
#Task6       
if number1 > 5 or (number2==7 and number3==7):
    print('Петя')