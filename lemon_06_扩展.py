#1、题目：企业发放的奖金根据利润提成（提示：用到的知识点：条件判断）
'''
用户输入利润
利润低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；
40万到60万之间时，高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分，可提成1.5%，高于
100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
'''
print("************第1题*****************")   
profit = int(input("请输入利润："))
if profit < 0:
    print("请输入正确的数")
elif 0 < profit<=10:
    bonus = profit * 0.1
elif 10< profit <20:
    bonus = 10*0.1+ (profit-10)*0.075
elif 20<= profit <40:
    bonus = 10*0.1+10*0.075+(profit-20)*0.05
elif 40<= profit <60:
    bonus = 10*0.1+10*0.075+20*0.05+(profit-40)*0.03
elif 60<= profit <100:
    bonus = 10*0.1+10*0.075+20*0.05+40*0.03+(profit-60)*0.015
else:
    bonus = 10*0.1+10*0.075+20*0.05+40*0.03+60*0.015+(profit-100)*0.01
print("应发放的奖金为：{}".format(bonus))

'''
作业2、编写一个文字版的自动售货机的代码，运行功能如下:
提示：用到的主要知识点，条件判断 、while循环
1、运行程序打印如下提示，
请用输入您购买的商品编号：

【1】可乐 2.5元​ 【2】雪碧 2.5元​ 【3】哇哈哈 3元​ 【4】红牛 6元​ 【5】脉动 4元​ 【6】果粒橙 3.5元

2、用户输入选择之后，打印如下格式的提示：您购买的是XX，需要支付金额为XX元
3、打印：请投币（支持1元，5元，10元）
4、用户输入投币金额，判断用户输入金额是否大于商品价格
用户投币金额不够商品价格，继续提示投币，

当投币超过商品价格，则打印投币的金额和找零金额，然后结束程序
'''
print("************第2题*****************")   
while True:
    dic = {"1":2.5,"2":2.5,"3":3,"4":6,"5":4,"6":3.5}
    zhifu = 0
    choose = input("请选择您要购买的饮料为: 1: 可乐 2: 雪碧 3: 哇哈哈 4: 红牛 5: 脉动 6: 果粒橙")
    if choose == '1':
        print("你购买的是可乐，需要支付的钱数为：{}".format(dic[choose]))
    elif choose == '2':
        print("你购买的是雪碧，需要支付的钱数为：{}".format(dic[choose]))
    elif choose == '3':
        print("你购买的是哇哈哈，需要支付的钱数为：{}".format(dic[choose]))
    elif choose == '4':
        print("你购买的是红牛，需要支付的钱数为：{}".format(dic[choose]))
    elif choose == '5':
        print("你购买的是脉动，需要支付的钱数为：{}".format(dic[choose]))
    elif choose == '6':
        print("你购买的是果粒橙，需要支付的钱数为：{}".format(dic[choose]))
    else:
        print("退出程序")
    zhifu = dic[choose]
    li = [1,5,10]
    money = 0
    toubin = int(input("请投币：1:1元 2:5元 3:10元"))
    if toubin == 1:
        money = li[toubin-1]  
    elif toubin == 2:
        money = li[toubin-1]
    elif toubin == 3:
        money = li[toubin-1]
    else:
        print("投币错误，请重新投入")
        continue
    if zhifu > money:
        print("用户投币金额不够商品价格，继续提示投币，")
    elif zhifu <= money:
        shengyu = money - zhifu
        print("投币的金额为：{},找零的金额为：{}".format(money,shengyu))
        break
    else:
        print("支付失败")

#作业3:
#3、打印99乘法表，
print("************第3题*****************")   
for i in range(1,10):
    for j in range(1,i+1):
        print("%d*%d=%d"%(j,i,i*j),end=" ")
    print("")

#作业4、小明有100块钱 ，需要买100本书（钱要刚好花完），a类数5元一本，b类书3元一本，c类书 1元2本。请写一段代码计算小明有多少种购买的方式？
#思路提示：穷举法，使用技术点：for循环嵌套
print("************第4题*****************")    
li = []
for x in range(0,21):
    for y in range(0,34):
        for z in range(0,200):
            if 5*x + 3*y + 0.5*z ==100 and x + y + z == 100:
                print("购买a:{}本，b:{}本，c:{}本".format(x,y,z))
                li.append((x,y,z))
print(li)
print("一共有{}种购买方式".format(len(li)))



