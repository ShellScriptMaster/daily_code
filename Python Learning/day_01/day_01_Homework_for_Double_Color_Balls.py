# this is a number pick system
# users choose　6 number for Red Balls and 2 number for Blue Balls.
# While user make the decision, print out the number in a list for each color.
# the number　could not be repeated. If so , print out a Warning
# the number should not bigger than 36 . If so , print out a Warning.
# print out a 'Good luck' at last
REDBALLS = []
BULEBALLS = []
count = 0
# Pick RED
while  count < 6 :
    num = int(input('Please choose a number for RED'))
    if num > 36 or 0 > num:
        print('the number should not bigger than 36 or less than 0')
        continue
    else:
        if num in REDBALLS:
            print('number %d are already in REDBALLS' % num )
            continue
        else:
            REDBALLS.append(num)
            count += 1
            continue
# pick BULE
count = 0
while 2 > count  :
    num = int(input('what is your LUCKY NUMBER for BULE? '))
    if num > 36 or num < 0 :
        print('the number should not bigger than 36 or less than 0')
        continue
    else:
        if num in REDBALLS or num in BULEBALLS:
            print('number should not be repeated')
            continue
        else:
            BULEBALLS.append(num)
            count += 1
            continue
print('REDBALLS is '+ str(REDBALLS) )
print('BULEBALLS is ' + str(BULEBALLS))
print('good luck to you !!!!')

