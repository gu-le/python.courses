#!/bin/python3
from math import trunc
print("Введите ваш рост")
r=float(input())
print("Введите ваш вес")
w=float(input())
print("Введите ваш возраст")
age=int(input())
print("Введите 1 если вы мужчина, 2 если вы женщина ")
gender=int(input())
BMI=w/r**2
if age >= 18 and age <= 43 and BMI <=20 and gender==1:
    print('underweigth')
    print('больше кушай гамбургеров и пей колу')
    print('10','='*(50 - int(trunc(BMI))),'|','='*(50 - (50-int(trunc(BMI)))),'50')
    print("Ваш BMIndex от 10 до 50 равен ",BMI)
if age >= 18 and age <= 43 and BMI >20 and BMI <=28 and gender==1:
    print('norma')
    print('молодец, так держать!!!')
    print('10','='*(50 - int(trunc(BMI))),'|','='*(50 - (50-int(trunc(BMI)))),'50')
    print("Ваш BMIndex от 10 до 50 равен ",BMI)
if age >= 18 and age <= 43 and BMI >28 and gender==1:
    print('overweight')
    print('упс!!! пора бежать в спортзал')
    print('10','='*(50 - int(trunc(BMI))),'|','='*(50 - (50-int(trunc(BMI)))),'50')
    print("Ваш BMIndex от 10 до 50 равен ",BMI)
###
if age >= 44 and age <= 60 and BMI <=22 and gender==1:
    print('underweigth')
    print('больше кушай гамбургеров и пей колу')
    print('10','='*(50 - int(trunc(BMI))),'|','='*(50 - (50-int(trunc(BMI)))),'50')
    print("Ваш BMIndex от 10 до 50 равен ",BMI)
if age >= 44 and age <= 60 and BMI >22 and BMI <=29 and gender==1:
    print('norma')
    print('молодец, так держать!!!')
    print('10','='*(50 - int(trunc(BMI))),'|','='*(50 - (50-int(trunc(BMI)))),'50')
    print("Ваш BMIndex от 10 до 50 равен ",BMI)
if age >= 44 and age <= 60 and BMI >29 and gender==1:
    print('overweight')
    print('упс!!! пора бежать в спортзал')
    print('10','='*(50 - int(trunc(BMI))),'|','='*(50 - (50-int(trunc(BMI)))),'50')
    print("Ваш BMIndex от 10 до 50 равен ",BMI)
###
if age > 60 and BMI <=25 and gender==1:
    print('underweight')
    print('больше кушай гамбургеров и пей колу')
    print('10','='*(50 - int(trunc(BMI))),'|','='*(50 - (50-int(trunc(BMI)))),'50')
    print("Ваш BMIndex от 10 до 50 равен ",BMI)
if age > 60 and BMI >25 and BMI <=29 and gender==1:
    print('norma')
    print('молодец, так держать!!!')
    print('10','='*(50 - int(trunc(BMI))),'|','='*(50 - (50-int(trunc(BMI)))),'50')
    print("Ваш BMIndex от 10 до 50 равен ",BMI)
if age > 60 and BMI >29 and gender==1:
    print('overweight')
    print('упс!!! пора бежать в спортзал')
    print('10','='*(50 - int(trunc(BMI))),'|','='*(50 - (50-int(trunc(BMI)))),'50')
    print("Ваш BMIndex от 10 до 50 равен ",BMI)


###
###

if age >= 18 and age <= 43 and BMI <=21 and gender==2:
    print('underweigth')
    print('больше кушай гамбургеров и пей колу')
    print('10','='*(50 - int(trunc(BMI))),'|','='*(50 - (50-int(trunc(BMI)))),'50')
    print("Ваш BMIndex от 10 до 50 равен ",BMI)
if age >= 18 and age <= 43 and BMI >21 and BMI <=26.9 and gender==2:
    print('norma')
    print('молодец, так держать!!!')
    print('10','='*(50 - int(trunc(BMI))),'|','='*(50 - (50-int(trunc(BMI)))),'50')
    print("Ваш BMIndex от 10 до 50 равен ",BMI)
if age >= 18 and age <= 43 and BMI >26.9 and gender==2:
    print('overweight')
    print('упс!!! пора бежать в спортзал')
    print('10','='*(50 - int(trunc(BMI))),'|','='*(50 - (50-int(trunc(BMI)))),'50')
    print("Ваш BMIndex от 10 до 50 равен ",BMI)
###
if age >= 44 and age <= 60 and BMI <=23 and gender==2:
    print('underweigth')
    print('больше кушай гамбургеров и пей колу')
    print('10','='*(50 - int(trunc(BMI))),'|','='*(50 - (50-int(trunc(BMI)))),'50')
    print("Ваш BMIndex от 10 до 50 равен ",BMI)
if age >= 44 and age <= 60 and BMI >23 and BMI <=28 and gender==2:
    print('norma')
    print('молодец, так держать!!!')
    print('10','='*(50 - int(trunc(BMI))),'|','='*(50 - (50-int(trunc(BMI)))),'50')
    print("Ваш BMIndex от 10 до 50 равен ",BMI)
if age >= 44 and age <= 60 and BMI >28 and gender==2:
    print('overweight')
    print('упс!!! пора бежать в спортзал')
    print('10','='*(50 - int(trunc(BMI))),'|','='*(50 - (50-int(trunc(BMI)))),'50')
    print("Ваш BMIndex от 10 до 50 равен ",BMI)
###
if age > 60 and BMI <=24 and gender==2:
    print('underweight')
    print('больше кушай гамбургеров и пей колу')
    print('10','='*(50 - int(trunc(BMI))),'|','='*(50 - (50-int(trunc(BMI)))),'50')
    print("Ваш BMIndex от 10 до 50 равен ",BMI)
if age > 60 and BMI >24 and BMI <=29 and gender==2:
    print('norma')
    print('молодец, так держать!!!')
    print('10','='*(50 - int(trunc(BMI))),'|','='*(50 - (50-int(trunc(BMI)))),'50')
    print("Ваш BMIndex от 10 до 50 равен ",BMI)
if age > 60 and BMI >29 and gender==2:
    print('overweight')
    print('упс!!! пора бежать в спортзал')
    print('10','='*(50 - int(trunc(BMI))),'|','='*(50 - (50-int(trunc(BMI)))),'50')
    print("Ваш BMIndex от 10 до 50 равен ",BMI)

#


