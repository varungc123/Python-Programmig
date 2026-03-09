n=int(input("enter : "))
for i in range(n):
    for j in range(1,n-1):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
4