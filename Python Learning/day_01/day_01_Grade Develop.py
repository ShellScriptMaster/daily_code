# Mapping Level application
# here are five levels , which are A:90-100 B:80-89 C:60-79 D:40-59 E: 39<
# The function is when input a Grade, the App  will map the corresponding Level and print

Grade = int(input('what is your Grade?'))
if  Grade > 100 or Grade < 0:
    print('Illegal value')
elif 100 > Grade >= 90:
    print('Level A')
elif 90 > Grade >= 80:
    print('Level B')
elif 80 > Grade >= 60:
    print('Level C')
elif 60 > Grade >= 40:
    print('Level D')
else:
    print('Level E')