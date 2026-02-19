a=10                            #global variable
def fun1():
    global a
    a=100
    b=20                       #non local variable
    print(a)
    print(b)
    def fun2():
        global a
        nonlocal b
        a=1000
        b=200
        c=30                   #local variable
        print(a)
        print(b)
        print(c)
    fun2()
    print(a)
fun1()
class Demo:
    x=11                        #static variable
    def __init__(self):
        self.y=22               #instance variable
        self.z=33
    def display(self):
        print(self.y)
        print(self.z)
        a=10                   #local variable
        b=20
        c=a+b
        print(c)
d1=Demo()
print(Demo.x)
d1.display()
print(a)
