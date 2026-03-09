n=int(input("enter the num"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==n or j==1 or i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("2222222222222222222222222222222222222222222222222")
for i in range(1,n+1):
    for k in range(i,n):
        print(" ",end="")
    for j in range(1,i+1):
        if i==n or j==1 or i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("3333333333333333333333333333333333333333333333333333333333333333")
for i in range(n,1-1,-1):
    for j in range(1,i+1):
        if i==n or j==1 or i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("44444444444444444444444444444444444444444444444444444444444444444444")
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or j==n or i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()