

def findgcd(a,b):
    lower=a
    if b<a:
        lower = b  #setting the lowest number
    gcd=1
    for i in range(2, (lower+1)):
        if a%i==0 and b%i==0:
            gcd=i
    return gcd
num1=int(input("enter num 1 : "))
num2=int(input("enter num 2 : "))
res=findgcd(num1,num2)
print(f"the gcd of {num1} and {num2} is :{res}")

