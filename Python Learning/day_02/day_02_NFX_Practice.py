# 提示用户输入用户名和密码
# 获得到相关信息后，将其保存在变量中
# 如果用户输的用户名为 bob，密码为 123456，则输出 Login successful，否则输出 Login incorrect

# username = input('please input your username')
# password = input('please input your password')
# if username == 'bob' and password == '123456' :
#     print('login successfully')
# else:
#     print('login incorrect')
# ----------------------------------------------------------------------------------------------

# 如果成绩大于60分，输出“及格”
# 如果成绩大于70分，输出“良”
# 如果成绩大于80分，输出“好”
# 如果成绩大于90分，输出“优秀”
# 否则输出“你要努力了”

# Grade = int(input('your grade'))
# if 70 >= Grade > 60:
#     print('pass')
# elif 80 >= Grade > 70:
#     print('良')
# elif 90 >= Grade > 80:
#     print('good')
# elif Grade > 90:
#     print('excellent')
# else:
#     print('you have to work hard')
# ----------------------------------------------------------------------------------------------
# 编写石头剪刀布小游戏
# 计算机随机出拳
# 玩家自己决定如何出拳
# 代码尽量简化
# ------------------------------------------------------笨比代码------------------------------------------------------
# import  random
# all_choice = ['剪刀', '石头','布']
# computer = all_choice[random.randint(0,2)]
# player = input('请出拳(石头/剪刀/布)')
# if computer == player:
#     print('平局')
# elif computer == '剪刀':
#     if player == '石头':
#         print('玩家赢')
#     else:
#         print('computer win')
# elif computer == '石头':
#     if player == '布':
#         print('玩家赢')
#     else:
#         print('computer win')
# elif computer == '布':
#     if player == '剪刀':
#         print('玩家赢')
#     else:
#         print('computer win')
# ------------------------------------------------------流批代码------------------------------------------------------
# import random
#
# all_choice = ['剪刀', '石头', '布']
# computer = all_choice[random.randint(0, 2)]
# player = input('请出拳(石头/剪刀/布)')
# win_list = [['剪刀', '布'], ['石头', '剪刀'], ['布', '石头']]
# if computer == player:
#     print('平局')
# elif [computer,player] in win_list:
#     print('computer win')
# else:
#     print('player win')
# ------------------------------------------------------流批代码------------------------------------------------------
