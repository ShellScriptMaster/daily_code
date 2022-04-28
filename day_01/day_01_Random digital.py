#在0-10 以内猜数字
import random
Chance = 0
SET = random.randint(0, 10)
while  5 > Chance:
    Answer = int(input('what is your answer ?'))
    if SET < Answer:
        print(SET)
        print('Try Smaller')
    elif SET > Answer:
        print(SET)
        print('Try Bigger')
    else :
        print('Oh, you are Right !!!!! Bingo!!!!!!')
        break
    Chance += 1
print(SET)

#分隔
print('-' * 30 + 'END Random Testing' + '+' * 30)

# # print even number
print('-' * 30 + 'Here is the EVEN'  + '+' * 30)
#分隔

#输出0-100的偶数
count = 0
while  100 >= count :
    if count %2 == 0:
        print("%d" % count)
    count += 1
# print odd number  输出0-100的基数
print('-' * 30 + 'Here is the ODD ' + '+' * 30)
count = 0
while 100 >= count:
    if count % 2 == 1:
        print("%d" % count)
    count += 1

# the Correct Case  输出0-100的数，不输出10-20的数字
Digital = 0
while Digital < 100:
    Digital += 1
    if 20 > Digital > 10:
        continue
    print(Digital)


