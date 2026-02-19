def num(n):
    if n<=0:
       return
    print(n)
    num(n-1)   #here the function is called so it goes to first line again
    print(n)   #here everything goes back printing all n values.
n=int(input("enter num: "))
num(n)