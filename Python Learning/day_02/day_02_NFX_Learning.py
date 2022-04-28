if 3 > 0 :
    print('yes')
print('*' * 30, 'End Test', '+' * 30)
if -0.0:
    print('*' * 30, 'End Test', '+' * 30)
else:
    print('True')
print('*' * 30, 'End Test', '+' * 30)
if ' ':
    print('空格也是一个字符，Value = True')
print('*' * 30, 'End Test', '+' * 30)
if [False]:
    print('非空列表，Value = True')
print(bool([False]))
print(bool([0]))
print('*' * 30, 'End Test', '+' * 30)
if (10,20):
    print('元组为 True')
print('*' * 30, 'End Test', '+' * 30)
if {}:
    print('False')
else:
    print('True')
print('*' * 30, 'End Test', '+' * 30)
print(bool(None))
if not None:
    print('True') 
