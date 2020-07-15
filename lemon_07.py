#作业1 简单题
'''
1.函数的形参有三种形式:
必需参数：定义了就一定要传，个数不能多也不能少
默认参数：定义的时候可以设置默认值，调用的时候可以传，也可以不传
不定长参数（动态\可变参数）：可以接收0个或者多个参数
2. 函数的实参有两种形式：
位置参数：按照参数定义的位置进行传递
关键字参数：通过参数名字指定，

#作业2 利用上课讲的for循环嵌套的知识点，封装一个可以打印任意列的三角形的函数
* * * * * *
* * * * *
* * * *
* * * 
* *
*
'''
def  print_fun(n):
    for i in range(1,n+1):
        for j in range(i,n+1):
            print('*',end =' ')
        print()
print_fun(6)

#作业3.定义一个可以完成任意个数字相加的函数，（支持关键字传参和位置传参）并返回相加的结果

def add(*args,**kwargs):
    res = sum(args)+sum(kwargs)
    print(res)
add(1)
add(11,22)
add(11,22,33)
add(1,2,3,4,5)


def fun(*args,**kwargs):
    sum1 = 0
    for i in args:
        sum1 += i 
    for j in kwargs.values():
        sum1 += j
   
    print(sum1)
fun(1)
fun(11,22)
fun(1,2,3,4,5)
fun(1,2,3,4,5,a=11,b=22)