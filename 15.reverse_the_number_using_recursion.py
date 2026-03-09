def reverse(n,rev,temp):
    if n<=0:
        return rev==temp
    rem=n%10
    rev=(rev*10)+rem
    n=n//10
    return reverse(n,rev,temp)
n=int(input("number"))
flag=reverse(n,0,n)
if flag:
    print("true")
else:
    print("false")
