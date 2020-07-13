#作业1

'''
1、实现剪刀石头布游戏（），提示用户输入要出的拳 ：石头（1）／剪刀（2）／布（3）/退出（4） 电脑随机出拳比较胜负，显示 用户胜、负还是平局。
运行如下图所示（提示：while循环加条件判断，做判断时建议先分析胜负的情况）
user   random
1        2     1-2 =-1 
2        3     2-3= -1
3        1     3- 1 = 2
'''
print("************第一题*****************")   
import random

li =["石头","剪刀","布"]

while True:
    print('石头【1】 剪刀【2】 布【3】 游戏结束【4】')
    user = int(input("请输入上面的选项:"))
    rand = random.randint(1,3)
    print("电脑的输出为:{}".format(rand))
    if 1 <= user <=3: 
        if rand - user == -1 and rand - user == 2:
            print("用户输入为:{},电脑输入为:{},用户胜".format(li[user-1],li[rand-1]))
        elif rand == user:
            print("用户输入为:{},电脑输入为:{},平局".format(li[user-1],li[rand-1]))
        else:
            print("用户输入为:{},电脑输入为:{},电脑胜".format(li[user-1],li[rand-1]))
    elif user == 4:
        print("游戏结束")
        break
    else:
        print('您的出拳有误，请按规矩出拳！')

#作业2:
#通过定义一个计算器，允许程序提示用户输入数字1，数字2，然后再提示用户选择 ：   加【1】    减【2】    乘【3】      除【4】，
#根据不同的选择完成不同的计算 ，然后打印结果

print("************第二题*****************")   
while True:
    print('加【1】 减【2】 乘【3】 除【4】 退出【5】')
    oper = int(input("请输入上面的数:"))
    Num1 = float(input("请输入数字1："))
    Num2 = float(input("请输入数字2："))
    if 1 <= oper <= 4:
        if oper -1 == 0:
            print("两数相加:{}".format(Num1 + Num2))
        elif oper -1 == 1:
            print("两数相减:{}".format(Num1 - Num2))
        elif oper -1 == 2:
            print("两数相乘:{}".format(Num1 * Num2))
        else:
            print("两数相除:{}".format(Num1 / Num2))
    elif oper == 5:
        print("退出程序")
        break
    else:
        print("输入无效，请重新输入")

#3、第三题：请获取下面字典数据中的token，和reg_name
print("************第三题*****************")     
data = {
    "code": 0,
    "msg": "OK",
    "data": {
        "id": 74711,
        "leave_amount": 29600.0,
        "mobile_phone": "13367899876",
        "reg_name": "小柠檬666",
        "reg_time": "2019-12-13 11:12:53.0",
        "type": 0,
        "token_info": {
            "token_type": "Bearer",
            "expires_in": "2019-12-30 22:28:57",
            "token": "eyJhbGciOiJIUzUxMiJ9.eyJtZW1iZXJfaWQiOjc0NzExLCJleHAiOjE1Nzc3MTYxMzd9.eNMtnEWr57iJoZRf2IRsGDWm2GKj9LZc1J2SGRprAwOk7EPoJeXSjJwdh0pcVVJygHmsbh1TashWqFv1bvCVZQ"
        }
    },
    "copyright": "Copyright 柠檬班 © 2017-2019 湖南省零檬信息技术有限公司 All Rights Reserved"
}
dic = data['data']
dic2 = dic['reg_name']
print('reg_name的值是:',dic2)
dic3 = dic['token_info']['token']
print('token的值是：',dic3)

#作业4
#当前有一个列表 li = [1,21,33,221,432,121,44,21,22,,44,1,221],请完成如下要求！
#1、请先去除列表中的重复元素
#2、对去重后的列表进行升序排序
#3、遍历排序后列表，将元素为偶数的元素，添加到一个新列表中
print("************第四题*****************") 
li = [1,21,33,221,432,121,44,21,22,44,1,221]
set1 = set(li)
li1 = list(set1)
print(li1)
li1.sort()
print(li1)
li2 = [] 
for i in li1:
    if i % 2 == 0:
        print('此数为偶数')
        li2.append(i)
    else:
        print('此数为奇数')
print(li2)

#作业5:运行程序，提示用户依次输入三个整数x,y,z，请把这三个数由小到大输出。

print("************第五题*****************") 
li3 = []
x = int(input("请输入数字1："))
y = int(input("请输入数字2："))
z = int(input("请输入数字3："))
#方式一

li3.append(x)
li3.append(y)
li3.append(z)
li3.sort()
print("从小到大的顺序为：{}".format(li3))

#方式二
if x > y:
    if y > z:
        print("{}<{}<{}".format(z, y, x)) 
    elif y < z:
        if x > z:
            print("{}<{}<{}".format(y, z, x)) 
        elif x < z:
             print("{}<{}<{}".format(y, x, z)) 
elif x < y: 
    if x > z: 

        print("{}<{}<{}".format(y, x, z))  
    elif x < z:  
        if y > z:  
            print("{}<{}<{}".format(y, z, x))  
        elif z < y:  
            print("{}<{}<{}".format(y, z, x))  

#第6题、编写一个程序，使用for循环输出0-100（包括0和100）之间的偶数

print("************第六题*****************") 
res =[]
for i in range(0,101):
    if i % 2 == 0:
        res.append(i)
print(res)
#作业7 ：当前有一个字典｛"a":1,"b":22,"c":3,"d":4,"e":5 },
#请修改字典中所有键值对的值，新的值为原来的值乘10
print("************第七题*****************") 
dic = {"a":1,"b":22,"c":3,"d":4,"e":5 }
for i in dic.keys():
    dic[i] = dic[i]*10
print(dic)
    