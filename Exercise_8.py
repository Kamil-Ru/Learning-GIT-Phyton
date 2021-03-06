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
    
    while True:
        player_a = input(str(print('Player A\nPlease chose one:\n1. Rock\n2. Scissors\n3. Paper\n')))
        if player_a in ['1', '2', '3']:
            break
        
    while True:
        player_b = input(print('Player B\nPlease chose one:\n1. Rock\n2. Scissors\n3. Paper\n'))
        if player_b in ['1', '2', '3']:
            break

    if player_a == player_b:
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
