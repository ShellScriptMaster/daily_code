# 买包子
# Case.01 包子 1.5元一个，买10个，打印付款价格
price = 1.5
quantity = 10
Total = price * quantity
print(Total)

# Case.02 老板高兴，总价打9折，重新打印付款价格
Discount = Total * 0.9
print(Discount)
print('-'*30, '我是分隔线', '+'*30)
# 汇率转换
# 用户输入美元，编写程序，将美元转换成人民币
# 汇率换算：美元 -> 人民币
# 1美元 = 6.4435人民币
USD = float(input('how much USD'))
RMB = USD * 6.4435
print(RMB, '￥', sep='')
print('-'*30, '我是分隔线', '+'*30)

# 列表 list
alist = []
alist.insert(0,2)
alist.append(3)
alist.insert(0,0)
print(alist)
print('a' in alist)
print(0 in alist)