#作业1. 实现一个文件复制器的函数，通过给函数传入一个路径，复制该路径下面所有的文件（目录不需要复制）到当前目录
import os
def file_copy(file_path):
    #file_path ='/Users/zhangcaiyan/Desktop/Lemon_python/lemon_python_08'
    try:
        res = os.listdir(file_path)
        print(res)
        os.chdir(file_path)
    except Exception as e:
        print(e)
    else:
        for i in res:
            #file_path = os.path.join(path,i)
            if os.path.isfile(i):
                with open(i,'rb') as f:
                    #content = f.read()
                    #new_file = 'cp' + i
                    #new_file = os.path.join(path2,new_file)
                    with open(f'cp_{i}','wb') as f1:
                        content = f.read()
                        f1.write(content)
            
file_path ='/Users/zhangcaiyan/Desktop/Lemon_python/lemon_python_08'
file_copy(file_path)
#file_copy(r:"/Users/zhangcaiyan/Desktop/Lemon_python/lemon_python_08")


#作业2 优化之前的作业的石头剪刀布游戏，用户输入时，如果输入非数字会引发异常，请通过异常捕获来处理这个问题

print("************第二题*****************")   
import random

li =["石头","剪刀","布"]
while True:
    rand = random.randint(1,3)
    print("电脑的输出为:{}".format(rand))
    print('石头【1】 剪刀【2】 布【3】 游戏结束【4】')
    try:
        user = int(input("请输入上面的选项:"))
    except ValueError as e:
        print("输入错误，请重新输入")
        continue
    else:
        
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
            print("输入错误")
