#作业1: 请封装一个函数，按要求实现数据的格式转换
#传入参数：data = ["{'a':11,'b':2}","[11,22,33,44]"]
#返回结果：res = [{'a':11,'b':2},[11,22,33,44]]
#通过代码将传入参数转换为返回结果所需数据，然后返回
print("*********第一题**********")
res = []
def func(li):
    for i in li:
        res.append(eval(i))
    return res
    print(res)
data = ["{'a':11,'b':2}","[11,22,33,44]"]
func(data)   
'''
#作业2:请封装一个函数。完成如下数据格式转换
#传入参数：
cases = [
    ['case_id','case_title','url','data','expected'],
    [1,'用例1','www.baidu.com','001','ok'],
    [2,'用例2','www.baidu.com','002','ok'],
    [3,'用例3','www.baidu.com','002','ok'],
    [4,'用例4','www.baidu.com','002','ok'],
    [5,'用例5','www.baidu.com','002','ok'],
]
#返回结果：
cases02 = [
    {'case_id':1,'case_title':'用例1','url':'www.baidu.com','data':'001','expected':'ok'},
    {'case_id':2,'case_title':'用例2','url':'www.baidu.com','data':'002','expected':'ok'},
    {'case_id':3,'case_title':'用例3','url':'www.baidu.com','data':'002','expected':'ok'},
    {'case_id':4,'case_title':'用例4','url':'www.baidu.com','data':'002','expected':'ok'},
    {'case_id':5,'case_title':'用例5','url':'www.baidu.com','data':'002','expected':'ok'}
]
'''
print("*********第二题**********")
cases02 = []
def fun(li):
    for item in li[1:]:
        dic = dict(zip(li[0],item))
        cases02.append(dic)
    return cases02
    print(cases02)
    

cases = [
    ['case_id','case_title','url','data','expected'],
    [1,'用例1','www.baidu.com','001','ok'],
    [2,'用例2','www.baidu.com','002','ok'],
    [3,'用例3','www.baidu.com','002','ok'],
    [4,'用例4','www.baidu.com','002','ok'],
    [5,'用例5','www.baidu.com','002','ok'],
]
fun(cases)