# Single Branch
print('-' * 15 + 'Start to Single Branch Testing' + '-' * 40)
weather = input('what is the weather today? ')
if weather == 'sun':
    print('sunshine')
else:
    print('rain_day')
print('-' * 40 + 'Single Branch Testing is finished ' + '-' * 40)
print("\n" )
print('-' * 40 + 'Start to Multiple Branch Testing ' + '-' * 40)
# Guess age
age = int(input('how old are you'))
if age < 12:
    print('you are a child')
elif age < 18:
    print('you are teenager')
elif age < 30:
    print('you are a young man')
else:
    print('you are a oil middle-age man')