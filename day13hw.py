################HW###################

#Q.Take score of two players as input,compare the scores and print the winner using IF..ELSE Statement

playerOne = input('Enter the name of player1:')
playerTwo = input('Enter the name of player2:')
score_playerOne = int(input('Enter the score of player1: '))
score_playerTwo = int(input('Enter the score of player2: '))

if(score_playerOne>score_playerTwo):
    print('The winner is', playerOne)
else:
    print('The winner is', playerTwo)
             



