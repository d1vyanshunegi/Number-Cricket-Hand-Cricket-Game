import random


def toss():
    '''Coin toss to choose innings'''
    print('************************ M A T C H   S T A R T ************************')
    while True:
        userChoice = input('Heads or Tails(H/T)??:').upper()
        if userChoice != 'H' and userChoice != 'T':
            print("Invalid Input!")
            continue
        break
    if userChoice == random.choice(('H', 'T')):
        print('You won the toss!')
        while True:
            inningChoice = input('Press 1 to Bat; 0 to Bowl:')
            if inningChoice != '1' and inningChoice != '0':
                print('Enter a valid choice')
                continue
            break
        if inningChoice == '1':
            print("You chose to bat first!")
        else:
            print('You chose to bowl first!')
        return int(inningChoice)
    else:
        print('You lost the toss!')
        inningChoice = random.choice((1, 0))
        if inningChoice == 1:
            print('Comp chose to bat first!')
            return 0
        else:
            print('Comp chose to bowl first!')
            return 1


def bowling(target=None):
    '''Player is bowling'''
    compScore = 0
    compThrow = None
    playerThrow = -9
    if target == None:
        while compThrow != playerThrow:
            compThrow = random.randrange(0, 7)
            playerThrow = input('Your throw(between 0-6):')
            if playerThrow == '0' or playerThrow == '1' or playerThrow == '2' or playerThrow == '3' or playerThrow == '4' or playerThrow == '5' or playerThrow == '6':
                pass
            else:
                print('Invalid throw!')
                continue
            print(f'Comp threw:{compThrow}')
            if compThrow == int(playerThrow):
                break
            compScore += compThrow
            print(f'Comp Score:{compScore}')
        if compThrow == int(playerThrow):
            print('OUT!')
        return compScore
    else:
        while compThrow != playerThrow:
            compThrow = random.randrange(0, 7)
            playerThrow = input('Your throw(between 0-6):')
            if playerThrow == '0' or playerThrow == '1' or playerThrow == '2' or playerThrow == '3' or playerThrow == '4' or playerThrow == '5' or playerThrow == '6':
                pass
            else:
                print('Invalid throw!')
                continue
            print(f'Comp threw:{compThrow}')
            if compThrow == int(playerThrow):
                break
            compScore += compThrow
            print(f'Comp Score:{compScore}')
            if compScore >= target:
                break
        if compThrow == int(playerThrow):
            print('OUT!')
        return compScore


def batting(target=None):
    '''Player is batting'''
    playerScore = 0
    playerThrow = None
    compThrow = -9
    if target == None:
        while playerThrow != compThrow:
            compThrow = random.randrange(0, 7)
            playerThrow = input('Your throw(between 0-6):')
            if playerThrow == '0' or playerThrow == '1' or playerThrow == '2' or playerThrow == '3' or playerThrow == '4' or playerThrow == '5' or playerThrow == '6':
                pass
            else:
                print('Invalid throw!')
                continue
            print(f'Comp threw:{compThrow}')
            if int(playerThrow) == compThrow:
                break
            playerScore += int(playerThrow)
            print(f'Your Score:{playerScore}')
        if int(playerThrow) == compThrow:
            print('OUT!')
        return playerScore
    else:
        while playerThrow != compThrow:
            compThrow = random.randrange(0, 7)
            playerThrow = input('Your throw(between 0-6):')
            if playerThrow == '0' or playerThrow == '1' or playerThrow == '2' or playerThrow == '3' or playerThrow == '4' or playerThrow == '5' or playerThrow == '6':
                pass
            else:
                print('Invalid throw!')
                continue
            print(f'Comp threw:{compThrow}')
            if int(playerThrow) == compThrow:
                break
            playerScore += int(playerThrow)
            print(f'Your Score:{playerScore}')
            if playerScore >= target:
                break
        if int(playerThrow) == compThrow:
            print('OUT!')
        return playerScore


def playMatch():
    '''Starts the game'''
    tossResult = toss()

    if tossResult == 1:
        playerScore = batting()
        target = playerScore+1
        print(f'Your score:{playerScore}\nComp needs {target} runs to win.\n')
        print("Your innings to bowl!")
        compScore = bowling(target)
    else:
        compScore = bowling()
        target = compScore+1
        print(f'Comp scored:{compScore}\nYou need {target} runs to win.')
        print("Your innings to bat!")
        playerScore = batting(target)

    print('************************ SCORE CARD ************************')
    print(f'Your Score:{playerScore}\nComp Score:{compScore}')
    print('************************************************')
    if playerScore > compScore:
        print('You Won!')
    elif compScore > playerScore:
        print('You Lost!')
    else:
        print('Match Draw!')
    print('************************************************')


while True:
    '''Loop to get user input to continue playing or not'''
    playMatch()
    while True:
        x = input('Play again(Y/N)??:').upper()
        if x == 'Y':
            break
        elif x == 'N':
            exit()
        else:
            print('Enter a valid input')
            continue
