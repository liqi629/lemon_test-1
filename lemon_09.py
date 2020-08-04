'''
#作业1 当前有个txt文件，要求：将数据读取出来，转换为如下的格式
#{'data0':‘数据aaa','data1':'数据bbb','data2':'数据ccc','data3':'数据ddd'}
li = []
dic = {}
with open('lemon_python_08//test.txt','r',encoding ='utf-8') as f:
    content = f.readlines()
    for i in content:
        res = i.replace('\n','')
        li.append(res)
    for k,v in enumerate(li):
        dic[f'data{k}'] = v
print(dic)
#作业2 当前有一个case.txt文件，里面存储了很多用例数据，每一行数据就是一条用例数据，
#要求一：请把这些数据读取出来，并且存到list中，格式如下：
li2 = []
dic = {}
li3 = []
dic2 = {}
data = ['data1','data2','data3','data4','data5']

with open ('lemon_python_08//case.txt','r',encoding = 'utf-8') as f1:
    content = f1.readlines()
    for i in content:
        res = i.replace('\n','')
        str = res.split(',')
        for j in str:
            es = j.split(':')
            li2.append(tuple(es))
        dic = dict(li2)
        li3.append(dic)
    print(li3)
    for k,v in enumerate(li3):
        dic2[f'data{k}'] = v
print(dic2)
'''
#作业3: 之前上课讲了一个注册功能的案例，在之前的案例功能上进行升级
#要求 把所有用户数据放到文件中进行保存，数据存储格式不限，
import json

'''
users = [
    {"uid": "py01", "pwd": "lmb01"},
    {"uid": "py02", "pwd": "lmb02"},
    {'uid': 'cathy', 'pwd': 'cy0609'}
    {"uid": "cathy", "pwd": "0908"}
    {"uid": "eason", "pwd": "0908"}
]
'''
us = []
users = []
try:
    with open('lemon_python_08//user_info.txt','r',encoding ='utf-8') as f1:
        content = f1.readlines()
    for i in content:
        es = i.replace('\n','')
        us.append(es)
    for j in us:
        res = eval(j)
        users.append(res)
    print(users)

except FileNotFoundError as e:
    print("文件不存在")
    users = []


id = input("请输入账号：")
pwd = input("请输入密码：")
pwd2 = input("请再次确认密码：")
# 遍历所有的账号
for u in users:
    # 判断账号是否已经被注册
    if id == u["uid"]:
        print("该账号已经被注册！")
        break
else:
    # 如果账号没有注册，那么for循环中的break不会执行。则会执行for对应的else语句
    print("该账号可以注册，继续判断密码！")
        # 判断两次密码是否一致
    if pwd == pwd2:
        print("注册成功！")
        # 帮输入的账号密码已字典的形式加入道users中
        users.append({"uid": id, "pwd": pwd})

    else:
        print("两次输入的密码不一致")

str2 = str(users)
with open('lemon_python_08//user_info.txt','a',encoding ='utf-8') as f2:
    f2.write(str2+"\n")





