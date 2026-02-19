def findgcd(n1,n2):
    lower=n1
    if n2<n1:
        lower = n2  #setting the lowest number
    gcd=1
    for i in range(2, (lower+1)):
        if n1%i==0 and n2%i==0:
            gcd=i
    return gcd
def iscoprime(n1,n2):
    if findgcd(n1,n2)==1:
        return True
    else:
        return False


num1=int(input("enter num 1 : "))
num2=int(input("enter num 2 : "))
result1=findgcd(num1,num2)
result=iscoprime(num1,num2)
print(result1)
print(result)

