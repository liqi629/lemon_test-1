#1.现有字符串 str1 = "PHP is the best，programming,language in, the world!"
#要求一： 将指定的字符串PHP替换为Pyhton 
str1 =  "PHP is the best，programming,language in, the world!"
str2 = str1.replace('PHP','Python')
print(str2)
#要求二:上述替换以后，将字符串以逗号为分割点进行分割得到一个列表
str3 = str2.split(',')
print(str3)

#2.编写代码，提示用户输入1-7七个数字，分别代表周一到周日，打印输出“今天是周X”
week = ["周一","周二","周三","周四","周五","周六","周日"]
X = int(input("请输入1-7的数字："))
print("今天是周{}".format(week[X-1]))

#3.用户输入一个数值，请使用比较运符确认用户输入的是否为偶数，是偶数输出True,不是输出False
num = int(input("请输入一个数："))
f = num %2
print(F"取余运算后为{f}")
#方式一：
print(f == 0)
#方式二：
if f == 0:
    print(True,F"{num}是偶数")
else:
    print(False,F"{num}是奇数")

#4.现有一个字符串 s ="abcdefghijk",
#要求1：通过切片获取：defg
#要求2: 通过切片获取:cgk
s = "abcdefghijk"
#正向切片
print(s[3:7])
#指定终止位置
print(s[2:11:4])
#不指定终止位置
print(s[2: :4])
#反向切片
print("输出的字符串为:{}".format(s[3:-4]))
#要求3.通过切片获取 li = [2,3,1,4,6,2,5,6,7]中的[1,4,6,2]
li = [2,3,1,4,6,2,5,6,7]
print(li [2:6])
