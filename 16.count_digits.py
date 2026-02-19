def count_digits(n,count):
    if n<=0:
        return count
    n=n//10
    count=count+1
    return count_digits(n,count)


n=int(input("enter num :  "))
res=count_digits(n,0)
print(res)