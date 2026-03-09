n=int(input("enter the num"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==n or i==1 or j==1 or j==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
