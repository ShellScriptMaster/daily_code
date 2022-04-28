# you can guess the answer for no more than 3 times .
# If you can't get the correct answer after 3 chances ,
# input 'Y' or 'y' to acquire another 3 time chances, or input 'N' or 'n' to exit.
# The quantity of chances is unlimited
# When you get the correct answer, print 'congratulation' , then exit.
import random
chance = 0
age = random.randint(0, 99)
while 3 >= chance:
    chance += 1
    if 3 >= chance:
        Guess = int(input('what is your answer?'))
        if age < Guess:
            print('try SMALLER')
            continue
        elif age > Guess:
            print('try BIGGER')
            continue
        elif age == Guess:
            print('congratulations !!!!! ')
            print('the answer is %s' % age)
            break
    elif 3 < chance:
        Y_OR_N = input('do you want to continue? input Y or N')
        if Y_OR_N == 'y' or Y_OR_N == 'Y':
            chance = 0
            continue
        elif Y_OR_N == 'n' or Y_OR_N == 'N':
            break
        else :
            print('illegal value')
            chance = 3
            continue


