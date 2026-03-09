def findhcf(n1,n2):
    if n1 == 0:
        return  n2
    if n1 < n2:
        n1,n2=n2,n1
    return findhcf((n1 % n2),n2)
n1=int(input("enter the first number : "))
n2=int(input("enter the second number : "))
ans=findhcf(n1,n2)
print(ans)