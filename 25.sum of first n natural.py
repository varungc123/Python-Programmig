def sum(n):
    if n<=1:
        return 1
    return n+sum(n-1)
num=int(input("enter number : "))
res=sum(num)
print(f"the factorial of {num} is {res}")