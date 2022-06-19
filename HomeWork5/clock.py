import sys
import time
import datetime
import os
from time import strftime


def clear(): return os.system('clear')


run = True

zero = \
    ['⬛⬜⬜⬜⬜⬜⬛',
     '⬛⬜⬛⬛⬛⬜⬛',
     '⬛⬜⬛⬛⬛⬜⬛',
     '⬛⬜⬛⬛⬛⬜⬛',
     '⬛⬜⬛⬛⬛⬜⬛',
     '⬛⬜⬛⬛⬛⬜⬛',
     '⬛⬜⬜⬜⬜⬜⬛']

one =\
    ['⬛⬛⬛⬜⬛⬛⬛',
     '⬛⬛⬜⬜⬛⬛⬛',
     '⬛⬛⬛⬜⬛⬛⬛',
     '⬛⬛⬛⬜⬛⬛⬛',
     '⬛⬛⬛⬜⬛⬛⬛',
     '⬛⬛⬛⬜⬛⬛⬛',
     '⬛⬜⬜⬜⬜⬜⬛']

two =\
    ['⬛⬜⬜⬜⬜⬜⬛',
     '⬛⬜⬛⬛⬛⬜⬛',
     '⬛⬛⬛⬛⬜⬛⬛',
     '⬛⬛⬛⬜⬛⬛⬛',
     '⬛⬛⬜⬛⬛⬛⬛',
     '⬛⬜⬛⬛⬛⬛⬛',
     '⬛⬜⬜⬜⬜⬜⬛']

three =\
    ['⬛⬜⬜⬜⬜⬜⬛',
     '⬛⬛⬛⬛⬛⬜⬛',
     '⬛⬛⬛⬛⬛⬜⬛',
     '⬛⬛⬜⬜⬜⬜⬛',
     '⬛⬛⬛⬛⬛⬜⬛',
     '⬛⬛⬛⬛⬛⬜⬛',
     '⬛⬜⬜⬜⬜⬜⬛']

four =\
    ['⬛⬜⬛⬛⬛⬜⬛',
     '⬛⬜⬛⬛⬛⬜⬛',
     '⬛⬜⬛⬛⬛⬜⬛',
     '⬛⬜⬜⬜⬜⬜⬛',
     '⬛⬛⬛⬛⬛⬜⬛',
     '⬛⬛⬛⬛⬛⬜⬛',
     '⬛⬛⬛⬛⬛⬜⬛']

five =\
    ['⬛⬜⬜⬜⬜⬜⬛',
     '⬛⬜⬛⬛⬛⬛⬛',
     '⬛⬜⬛⬛⬛⬛⬛',
     '⬛⬜⬜⬜⬜⬜⬛',
     '⬛⬛⬛⬛⬛⬜⬛',
     '⬛⬛⬛⬛⬛⬜⬛',
     '⬛⬜⬜⬜⬜⬜⬛']

six =\
    ['⬛⬜⬜⬜⬜⬜⬛',
     '⬛⬜⬛⬛⬛⬛⬛',
     '⬛⬜⬛⬛⬛⬛⬛',
     '⬛⬜⬜⬜⬜⬜⬛',
     '⬛⬜⬛⬛⬛⬜⬛',
     '⬛⬜⬛⬛⬛⬜⬛',
     '⬛⬜⬜⬜⬜⬜⬛']


seven =\
    ['⬛⬜⬜⬜⬜⬜⬛',
     '⬛⬛⬛⬛⬛⬜⬛',
     '⬛⬛⬛⬛⬜⬜⬛',
     '⬛⬛⬛⬜⬛⬛⬛',
     '⬛⬛⬜⬛⬛⬛⬛',
     '⬛⬛⬜⬛⬛⬛⬛',
     '⬛⬛⬜⬛⬛⬛⬛⬛']


eight =\
    ['⬛⬜⬜⬜⬜⬜⬛',
     '⬛⬜⬛⬛⬛⬜⬛',
     '⬛⬜⬛⬛⬛⬜⬛',
     '⬛⬜⬜⬜⬜⬜⬛',
     '⬛⬜⬛⬛⬛⬜⬛',
     '⬛⬜⬛⬛⬛⬜⬛',
     '⬛⬜⬜⬜⬜⬜⬛']


nine =\
    ['⬛⬜⬜⬜⬜⬜⬛',
     '⬛⬜⬛⬛⬛⬜⬛',
     '⬛⬜⬛⬛⬛⬜⬛',
     '⬛⬜⬜⬜⬜⬜⬛',
     '⬛⬛⬛⬛⬛⬜⬛',
     '⬛⬛⬛⬛⬛⬜⬛',
     '⬛⬜⬜⬜⬜⬜⬛']


double_points =\
    ['⬛',
     '⬜',
     '⬜',
     '⬛',
     '⬜',
     '⬜',
     '⬛']


zero_separator =\
    ['⬛',
     '⬛',
     '⬛',
     '⬛',
     '⬛',
     '⬛',
     '⬛']


def display_time(numb1, numb2, s1, numb3, numb4, s2, numb5, numb6):
    print(numb1[0]+numb2[0]+s1[0]+numb3[0]+numb4[0]+s2[0]+numb5[0]+numb6[0])
    print(numb1[1]+numb2[1]+s1[1]+numb3[1]+numb4[1]+s2[1]+numb5[1]+numb6[1])
    print(numb1[2]+numb2[2]+s1[2]+numb3[2]+numb4[2]+s2[2]+numb5[2]+numb6[2])
    print(numb1[3]+numb2[3]+s1[3]+numb3[3]+numb4[3]+s2[3]+numb5[3]+numb6[3])
    print(numb1[4]+numb2[4]+s1[4]+numb3[4]+numb4[4]+s2[4]+numb5[4]+numb6[4])
    print(numb1[5]+numb2[5]+s1[5]+numb3[5]+numb4[5]+s2[5]+numb5[5]+numb6[5])
    print(numb1[6]+numb2[6]+s1[6]+numb3[6]+numb4[6]+s2[6]+numb5[6]+numb6[6])


def check_separator(value):
    if value == '1' or value == '3' or value == '5' or value == '7' or value == '9':
        return(zero_separator)
    else:
        return(double_points)


def check_number(value):
    match value:
        case '1':
            return(one)
        case '2':
            return(two)
        case '3':
            return(three)
        case '4':
            return(four)
        case '5':
            return(five)
        case '6':
            return(six)
        case '7':
            return(seven)
        case '8':
            return(eight)
        case '9':
            return(nine)
        case '0':
            return(zero)
        case _:
            return('error')


while run == True:
    time_now = str(strftime("%H:%M:%S"))
    time.sleep(1)
    clear()
    #print(time_now)
    display_time(check_number(time_now[0]), check_number(time_now[1]), check_separator(time_now[7]), check_number(
        time_now[3]), check_number(time_now[4]), check_separator(time_now[7]), check_number(time_now[6]), check_number(time_now[7]))


'''
    time_now = strftime("%H:%M:%S")
    time.sleep(1)
    sys.stdout.write("\r"+time_now)
    sys.stdout.flush()
'''
'''
for i in range(100):
    time.sleep(1)
    sys.stdout.write("\r%d%%" % i)
    sys.stdout.flush()
'''
