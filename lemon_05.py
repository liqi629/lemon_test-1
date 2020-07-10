import random
# 作业1: 有下面几个数据，t1 = (“aa”,11) t2 = (“bb”,22) li1 =[("cc",22)],变成如下的字典{"aa":11,"cc":22,"bb":22}
t1 = ('aa',11) 
t2 = ('bb',22) 
li1 =[("cc",22)]
#方式一：字典是无序的，我的理解只要键值对是一样的，前后无所谓
'''
li1.append(t1)
li1.append(t2)
print(li1)
dic = dict(li1)
print(dic)

#方式二：
li1.append(t2)
t3 = set(li1)
dic = dict([t1])
dic.update(t3)
print(dic)
'''
#方式三
#dic = dict([t1,li1[0],t2])
#print(dic)
dic = {}
li = list(t1)

dic[li[0]] = li[1]
dic[t2[0]]

#作业2:当前有一个列表 li = [11,22,33,22,22,44,55,77,88,99,11]要求一：去除列表的重复元素
#要求二：去重后删除77，88，99这三个元素
li = [11,22,33,22,22,44,55,77,88,99,11]
li2 = list(set(li))
#print(li2)
li2.sort()
#方式一：remove
li2.remove(77)
li2.remove(88)
li2.remove(99)
print(li2)
#方式二：pop
for i in range(3):
    li2.pop(-1)
print(li2)



#作业3:利用random函数生成随机整数（范围1-9），然后用户输入一个数字，来进行比较：
#如果大于随机数，则打印大于随机数
#如果小于随机数，则打印小于随机数 
#如果等于随机数，则打印等于随机数

Num1 = random.randint(1,9)
print(Num1)
Num2 = float(input("请输入一个数："))
if Num2> Num1:
    print("大于随机数")
elif Num2 < Num1:
    print("小于随机数")
elif Num2 == Num1:
    print("等于随机数")
else:
    print("输入无效")
print("程序执行结束")


#作业4:一家商场在降价促销，如果购买金额50-100元（包含50和100）之间，会给打九折
#如果购买金额大于100元，会给打八折，编写程序，询问购买金额，再打印出折扣和最终价格
money = float(input("请输入购买的金额："))
if 0<money<50:
    print("打折的折扣是0，需要花:{}".format(money))
elif 50<=money<=100:
    print("打折的折扣是:9折，需要花：{}".format(money*0.9))
elif money>100:
    print("打折的折扣是:8折，需要花：{}".format(money*0.8))
else:
    print("输入无效")
print("程序执行结束")

#作业5:提示用户输入一个整数（只考虑整数），判断这个数能同时被3和5整除
#能整除打印：能整除
#不能整除打印：不能整除
Num = int(input("请输入一个整数："))
if Num%3 == 0 and Num%5 == 0:
    print("能够整除")
else:
    print("不能整除")
