#作业1. 现有一个列表li2 =[1,2,3,4,5] 
#第一步：请通过三行代码将上面的列表，改成li2 = [0,1,2,3,66,5,11,22,33]
li2 =[1,2,3,4,5]
li2.insert(0,0)
li2[4] = 66
li2.extend([11,22,33])
print(li2)
#第二步：对列表进行升序排序（从小到大）
li2.sort()
print(li2)
#第三步：将列表复制一份进行降序排序（从大到小）
li3 = li2.copy()
li3.sort(reverse = True)
print(li3)
#作业2. 定义一个空列表user = [],分别提示用户输入姓名，年龄，身高，用户输入完后，将输入的信息作为添加到列表中保存，然后按照以下格式输出：
#用户的姓名为：XXX，年龄为：XXX，身高为：XXX，请仔细核对
#首先定义一个空的列表
user = []
name = input("请输入您的姓名为：")
age = int(input("请输入您的年龄为："))
height = int (input("请输入您的身高为："))
#添加到列表中
user.append(name)
user.append(age)
user.append(height)
#或者用extend
user.extend([name,age,height])
#方式一
print("用户的姓名为：{},年龄为:{},身高为:{}".format(user[0],user[1],user[2]))
#方式二
print(F"用户的姓名为：{user[0]},年龄为:{user[1]},身高为:{user[2]}")
#作业3.将字符串中的单词反转，“hello xiao mi"转换为“mi xiao hello"
str1 = "hello xiao mi"
#字符串以空格进行分割
li4 = str1.split(' ')
#列表进行反转
li4.reverse()
#print(li4)
#拼接成字符串
str2 = " ".join(li4)
print("输出的字符串为：{}".format(str2))
#作业4.字典的增删查改操作，某个比赛需要获取你的个人信息，编写一段代码要求如下
#1.运行是分别提醒用户输入姓名，性别，年龄，输入完了，请将数据通过字典保存起来
name = input("请输入您的姓名为：")
gender = input("请输入您的性别：")
age = int(input("请输入您的年龄为："))
dic = dict(姓名 = name,性别 = gender,年龄 = age)
print(dic)
#2.数据存储完了，然后输出个人介绍，格式如下：我的名字XXX，今年XXX岁，性别XXX，喜欢敲代码
#方式一：get方法
print(F"我的名字{dic.get('姓名')},今年{dic.get('年龄')}岁,性别:{dic.get('性别')},喜欢敲代码")
#方式二：通过键
print(F"我的名字{dic['姓名']},今年{dic['年龄']}岁,性别{dic['性别']},喜欢敲代码")
#3.平台需要你补足你的身高和联系方式（分别输入身高和联系方式到字典中）
height = int (input("请输入您的身高为："))
tel = input("请输入您的手机号码：")
dic ['身高'] = height
dic ['联系方式'] = tel
print(dic)
#4.平台为了保护你的隐私，需要你删除你的联系方式，下面两种方式任意选一个
#方式一：pop
dic.pop('联系方式')
print(dic)
#方式二：popitem
dic.popitem()
print(dic)
