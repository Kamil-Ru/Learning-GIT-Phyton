#   
#   Exercise 8
#   
#   Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), 
#   compare them, print out a message of congratulations to the winner, 
#   and ask if the players want to start a new game)
#   
#   Remember the rules:
#   
# -   Rock beats scissors
# -   Scissors beats paper
# -   Paper beats rock
#   
#   Concepts for this week:
# 
#   While loops
#   Infinite loops
#   Break statements


# 'Rock' = 1
# 'Scissors' = 2
# 'Paper' = 3 





def game():
    player_a = '0'
    player_b = '0'

    while player_a == '1' or '2' or '3':
        player_a = input(str((print('Player A\nPlease chose one:\n1. Rock\n2. Scissors\n3. Paper\n'))))
        # if player_a == '1' or '2' or '3':
        #     break
        # elif player_a != '1' or '2' or '3':
        #     print('You chose the wrong !!!\n\n')

    while player_b != '1' or '2' or '3':
        player_b = input(print('Player B\nPlease chose one:\n1. Rock\n2. Scissors\n3. Paper\n'))
        # if player_b == '1' or '2' or '3':
        #     break
        # elif player_b != '1' or '2' or '3':
        #     print('You chose the wrong !!!\n\n')


    if player_a == '1' and player_b == '1':
        print('You chose the same\n')
    elif player_a == '2' and player_b == '2':
        print('You chose the same\n')
    elif player_a == '3' and player_b == '3':
        print('You chose the same\n')
    elif player_a == '2' and player_b == '1':
        print('Player B has wonn\n')
    elif player_a == '3' and player_b == '1':
        print('Player A has wonn\n')
    elif player_a == '1' and player_b == '2':
        print('Player A has wonn\n')
    elif player_a == '1' and player_b == '3':
        print('Player B has wonn\n')


while True:
    menu = input(print('MENU \nPleas chose one:\n1. New game\n2. Quit\n'))
    if menu == '1':
        game()
    elif menu == '2':
        break








# while 



# Player_a = input(print('Player A\nPlease chose one:\n- Rock\n- Scissors\n- Paper\n'))
# Player_b = input(print('Player B\nPlease chose one:\n- Rock\n- Scissors\n- Paper\n'))
# if Player_a and Player_b is not a or b or c:
#     print('ERROR')
# else:
#     print('Player A = ' + str(Player_a) + '\nPlayer B = ' + str(Player_b))






