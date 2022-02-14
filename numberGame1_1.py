from random import randint


max_to = 10
minus_points = 3



def go_game(points):
    number_chosen = randint(1, max_to)
    current = 0

    print('\nStart!')
    print('\nPress enter\n')

    lose_win(number_chosen, current)

#     Wait_for_answer(answer)



def lose_win(number_chosen, current):
    write_yes = ( 'y', '', 'yes')
    write_no = ('n', 's', 'no', 'stop')

    global points
    global minus_points

    answer = str(input().lower(). replace(' ', ''))

    if answer in write_yes:
        current += 1
        if current <= number_chosen:
            lose_win(number_chosen, current)
        if current > number_chosen:
            if points > minus_points:
                points -= minus_points
                minus_points = 3
            else:
                points = 0
            print('\nYou lost(')
            main(points)
    if answer in write_no:
        win_amount = max_to - (number_chosen - current)
        points += win_amount
        if win_amount <= 2:
            minus_points += win_amount
        else:
            minus_points += win_amount // 5
        print('\nYou were ' + str(max_to - (number_chosen - current)) + " numbers away from losing :)")
        main(points)
    else:
        print('\nSorry, did not understand you' )
        lose_win(number_chosen, current)





"""setting max amount of number in game"""

def setting_max():
    global max_to

    try:
        answ = int(input('\ntipe maximum number you want to guess till (5-100) : '))
        if 5 <= answ <= 100:
            max_to = answ
            print('\nMax number setted as ' + str(max_to))
        else:
            print('\nTry again, put number between 5 and 100')
    except:
        print('\nSomething went wrong try again...')
    finally:
        main(points)




    """reading commands"""

def main(points):

    start_game = ('', 'start')
    set_max = ('setmax', 'set', 'max')
    save_prog = ('s', 'save')
    pts_words = ('pts', 'points', 'p')
    help_words = ('help', 'h')
    help_text = '''
    start - to start
    max - to set max
    save - to save points amount
    points - to see points amount
    '''

    print()

    answ = str(input().lower(). replace(' ', ''))

    if answ in start_game:
        go_game(points)
    if answ in set_max:
        setting_max()
    if answ in pts_words:
        print('\nYou have ' + str(points) + ' points' )
    if answ in help_words:
        print(help_text)
    if answ in save_prog:
        file_saver = open("numberGame_memory.txt", 'w')
        file_saver.write(str(points))
        file_saver.close()
        print("\nsaved!")

    main(points)







"""Start the code"""
points = 0
print('\ntipe "help" to see all commands')

try:
    file_saver = open("numberGame_memory.txt", 'r')
    points = int(file_saver.read())
    file_saver.close()
except ValueError:
    print("\nno saves founded")
    points = 0
    file_saver = open("numberGame_memory.txt", 'w')
    file_saver.write("0")
    file_saver.close()
except FileNotFoundError:
    file_saver = open("numberGame_memory.txt", 'w')
    file_saver.write("0")
    file_saver.close()

main(points)
