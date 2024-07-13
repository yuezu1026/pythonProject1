print("wkakwdkdk")


a={'name':'gaoqi','age':18}
b={'name':'gaoxixi'}
a.update(b)
print(a)

def mytest(name,age):
    print('my name is %s,my age is %d' %(name,age))

mytest('yasaka',19)


def mytest(name,age=18):
    print('my name is %s,my age is %d' %(name,age))

mytest('yasaka2',20)

mytest(name='dskdsk',age=2)
mytest(age=21,name='dskdsk')

#dfdskfk

def mytest(name,age,*hobby):
    print('my name is %s,my age is %d' %(name,age))
    print(hobby,len(hobby))
mytest('fdsfkds',19)
mytest('fdsfkds',19,'soccer','basketball','baseball')


def mytest(name,age,**hobby):
    print('my name is %s,my age is %d' %(name,age))
    print(hobby,len(hobby))
mytest('fdsfkds',19,first_hobby='basketball')


##递归
data = list(range(1,101))
print(data)
# sum = 0
# for x in data:
#     sum  += x
# sum
#
# print(sum)


def my_add(a,b):
    if len(a) == 2:
        return a[0] + a[1] + b
    return my_add(a[:-1],a[-1]) + b

a = my_add(data[:-1],data[-1])

print(a)


myseq=[128, 45.67, -6.2e8]
def mytest(num):
    return num * 2
print(mytest(10))
print(mytest(myseq))

myseq = [123,45.67,-6.2e8]

def convert(func,seq):
    print('转换序列中的数值,要他们同意为一样的数据类型')
    return [func(eachNum) for eachNum in seq]

print(convert(int,myseq))
print(convert(float,myseq))
print(convert(mytest,myseq))


def func_out(num1):
    def func_in(num2):
        return num1 + num2
    return func_in
f=func_out(10)
result=f(20)
print(result)

def log(func):
    def wrapper():
        func("牛郎和侄女相约鹊桥")
        func("牛郎和织女看电影")
        func("牛郎和侄女明年见")
    return wrapper

f = log(print)
f()






