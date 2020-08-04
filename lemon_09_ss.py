#读取文件
try:
    with open('lemon_python_08//user_info.txt','r',encoding ='utf-8') as f1:
        users = eval(f1.read())
except:
    users = []

id = input("请输入账号：")
pwd = input("请输入密码：")
pwd2 = input("请再次确认密码：")
# 遍历所有的账号
for user in users:
    # 判断账号是否已经被注册
    if id == user["uid"]:
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
#写入文件
str2 = str(users)
with open('lemon_python_08//user_info.txt','a',encoding ='utf-8') as f2:
    f2.write(str2+"\n")


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
#for i in range(len(li)):
#   dic['data{i}'.format(i)]= i.replace('\n','')
li2 = []
dic = {}
li3 = []
dic2 = {}
try:
    with open ('lemon_python_08//cases.txt','r',encoding = 'utf-8') as f1:
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
except:
    print("文件不存在")
     


