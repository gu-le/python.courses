#!/bin/python3
from math import trunc
print("Введите ваш рост")
r=float(input())
print("Введите ваш вес")
w=float(input())
BMI=w/r**2
print("Ваш BMIndex от 10 до 50 равен ",BMI)
print('10','='*(50 - int(trunc(BMI))),'|','='*(50 - (50-int(trunc(BMI)))),'50')

