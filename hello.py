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




