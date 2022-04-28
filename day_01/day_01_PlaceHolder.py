# placeholder
name = input('what is your name: ')
age = int (input('how old are you:'))
height = input('what is your height : ')
question = input('are you black ?')

msg = '''
---------------------Personal  Info------------------
name  : %s
age   : %d
height: %s
answer: %s
---------------------End-----------------------------
''' % (name,age, height, question)
print(msg)
if question == 'Y' or question == 'y':
    print('i don\'t believe it ')