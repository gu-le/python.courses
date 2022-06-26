#Реализация игры Tic-Tac-Toe для двух игроков на Python.

''' Мы будем делать доску, используя словарь
    в каких ключах будет местоположение (т.е.: верхний левый, средний правый и т. д.)
    и изначально его значения будут пустыми, а затем после каждого хода
    мы изменим значение в соответствии с выбором хода игрока.'''

theGameField = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

field_keys = []

statX=0
statO=0
tai=0

for key in theGameField:
    field_keys.append(key)

'''Нам придется распечатывать обновленную доску после каждого хода в игре и
    таким образом, мы создадим функцию, в которой мы определим функцию printBoard
    так что мы можем легко печатать доску каждый раз, вызывая эту функцию.'''

def printField(field):
    print(field['7'] + '|' + field['8'] + '|' + field['9'])
    print('-+-+-')
    print(field['4'] + '|' + field['5'] + '|' + field['6'])
    print('-+-+-')
    print(field['1'] + '|' + field['2'] + '|' + field['3'])

# Теперь мы напишем основную функцию, в которой есть весь игровой функционал.
def game():

    turn = 'X'
    count = 0


    for i in range(10):
        printField(theGameField)
        print("Ваш ход, " + turn + " в какое место переместить ?")

        move = input()        

        if theGameField[move] == ' ':
            theGameField[move] = turn
            count += 1
        else:
            print("Это место уже занято.\nВ какое место переместить?")
            continue

        # Теперь мы проверим, выиграл ли игрок X или O, для каждого хода после 5 ходов. 
        if count >= 5:
            if theGameField['7'] == theGameField['8'] == theGameField['9'] != ' ':
                printField(theGameField)
                print("\nКонец игры\n")                
                print(" **** " +turn + " Победитель ****")                
                break
            elif theGameField['4'] == theGameField['5'] == theGameField['6'] != ' ':
                printField(theGameField)
                print("\nКонец игры\n")                
                print(" **** " +turn + " Победитель ****")
                break
            elif theGameField['1'] == theGameField['2'] == theGameField['3'] != ' ':
                printField(theGameField)
                print("\nКонец игры\n")                
                print(" **** " +turn + " Победитель ****")
                break
            elif theGameField['1'] == theGameField['4'] == theGameField['7'] != ' ':
                printField(theGameField)
                print("\nКонец игры\n")                
                print(" **** " +turn + " Победитель ****")
                break
            elif theGameField['2'] == theGameField['5'] == theGameField['8'] != ' ':
                printField(theGameField)
                print("\nКонец игры\n")                
                print(" **** " +turn + " Победитель ****")
                break
            elif theGameField['3'] == theGameField['6'] == theGameField['9'] != ' ':
                printField(theGameField)
                print("\nКонец игры\n")                
                print(" **** " +turn + " Победитель ****")
                break 
            elif theGameField['7'] == theGameField['5'] == theGameField['3'] != ' ':
                printField(theGameField)
                print("\nКонец игры\n")                
                print(" **** " +turn + " Победитель ****")
                break
            elif theGameField['1'] == theGameField['5'] == theGameField['9'] != ' ':
                printField(theGameField)
                print("\nКонец игры\n")                
                print(" **** " +turn + " Победитель ****")
                break 

        # Если ни X, ни O не выиграют и доска будет заполнена, мы объявим результат «ничья».
        if count == 9:
            print("\nКонец игры\n")                
            print("Ничья")

        # Теперь нам нужно менять игрока после каждого хода.
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
    # Теперь мы спросим, хочет ли игрок перезапустить игру или нет.
    restart = input("Хотите играть снова?(y/n)")
    if restart == "y" or restart == "Y":  
        for key in field_keys:
            theGameField[key] = " "

        game()

if __name__ == "__main__":
    game()
    