 
import random
res= random.randint(10000000,99999999)
#随机生成131开头的手机号码
tel = "131" + str(res)
print("随机生成的手机号码是:",tel)
phone = 13100000000 + random.randint(10000000,99999999)
print("随机生成的手机号码是:{}".format(phone),"手机号码的长度是：{}".format(len(str(phone))))
# 2.变成一个字符串：'hello python18 !' 
a = 'hello'
b = 'python18'
c = '!'
res = ' '.join([a,b,c])
print("拼接后的字符串：",res)
print()
str = a + ' '+ b +' '+ c
#方式1
print(str)
#方式2
print("{} {} {}".format(a,b,c))
#方式3
print(f"{a} {b} {c}")
#方式4
print("%s %s %s"%(a,b,c))
#3.卖橘子的计算器
price = int(input("请输入橘子的价格："))
#购买的重量 保留一位小数
#随机生成购买的斤数（5到10之间的整数） 大于等于5 ，但小于10 
weight = random.randint(5,9) + random.random()
print("购买的重量为：%.1f"%weight)
#应该支付的金额
money = price * weight
# 保留支付金额到两位小数
print("橘子的单价是{},购买的重量是{},需要花{:.2f}".format(price,weight,money))
print(f"橘子的单价{price},购买的重量{weight},需要花{money}")
print("橘子的单价%s,购买的重量%.2f,需要支付%.2f"%(price,weight,money))

#4. 打印字符串，打印出来的字符串如下：PHP is the best""" \tprogramming"language in 'the\norld,实现方法：单引号包起来，然后特殊字符用斜线进行转义
s1 = 'PHP is the best\""" \\tprogramming\"language in \'the\\norld'
print(s1)
#关闭转义 字符串前加 r