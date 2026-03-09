print("1")
noc=1
n=int(input("enter the num"))
for i in range(1,2*n):
    for j in range(1,noc+1):
        if  j==noc or j==1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    if i<n:
        noc+=1
    else:
        noc-=1

print("2")
noc=1
n=int(input("enter the num"))
for i in range(1,2*n):
    for k in range(n,noc,-1):
        print(" ",end="")
    for j in range(1,noc+1):
        if  j==noc or j==1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    if i<n:
        noc+=1
    else:
        noc-=1

print("3")
noc=1
n=int(input("enter the num"))
for i in range(1,2*n):
    for k in range(n,noc,-1):
        print(" ",end="")
    for j in range(1,noc+1):
        if  j==noc or j==1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    if i<n:
        noc+=1
    else:
        noc-=1

print("4")
noc=n
n=int(input("enter the num"))
for i in range(1,2*n):
    for j in range(1,noc+1):
        if j==1 or i==(2*n)-1 or j==noc or i==1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    if i<n:
        noc-=1
    else:
        noc+=1


print("5")
noc=n
n=int(input("enter the num"))
for i in range(1,2*n):
    for k in range(n,noc,-1):
        print(" ",end="")
    for j in range(1,noc+1):
        if j==1 or i==(2*n)-1 or j==noc or i==1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    if i<n:
        noc-=1
    else:
        noc+=1

print("6")
noc=n
n=int(input("enter the num"))
for i in range(1,2*n):
    for k in range(n,noc,-1):
        print(" ",end="")
    for j in range(1,noc+1):
        if j==1 or i==(2*n)-1 or j==noc or i==1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    if i<n:
        noc-=1
    else:
        noc+=1


