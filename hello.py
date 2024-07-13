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
#dsfds

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
    def wrapper(a,b):
        func("%s和%s相约鹊桥"%(a,b))
        func("%s和%s女看电影"%(a,b))
        func("%s和%s明年见"%(a,b))
    return wrapper

log(print)("牛栏",'织女')
#f("牛栏",'织女')  #dfds

class Student(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def say_score(self):
        print(self.name,'的分数是:',self.score)

s1 = Student('zhang',90)
s1.say_score() #ddd

class Student(object):
    def __init__(self,temp_name,temp_age):
        self.name=temp_name
        self.age =temp_age
    def change_age(self,new_age):
        self.age = new_age
    def get_name(self):
        return self.name

s1 = Student('张三',18)
print(s1.age)
s1.change_age(20)
print(s1.name)
print(s1.age)
print(s1.get_name())

class Student(object):
    company = "尚学堂"
    count = 0
    def __init__(self):
        Student.count += 1

    @classmethod
    def printCompany(cls):
        print(cls.company)


s1 = Student()
s1 = Student()
s1 = Student()
print(s1.company)
print(s1.count)
Student.printCompany()











