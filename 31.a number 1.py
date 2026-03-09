print("==================================================")
n=int(input("enter"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()

print("==========================================================")
n=int(input("enter"))
for i in range(1,n+1):
    for j in range(n,i-1,-1):
        print(j,end=" ")
    print()

print("==========================================================")
noc=1
n=int(input("enter"))
for i in range(1,2*n):
    for j in range(n,noc-1,-1):
        print(j,end=" ")
    print()
    if i<n:
        noc+=1
    else:
        noc-=1

print("============================================================")
n=int(input("enter"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

print("============================================================")
n=int(input("enter"))
noc=1
for i in range(1,n*2):
    for j in range(1,noc+1):
        print(noc,end=" ")
    print()
    if i<n:
        noc+=1
    else:
        noc-=1

print("============================================================")
n=int(input("enter"))
for i in range(1,n+1):
    for j in range(i,n+i):
        print(j,end=" ")
    print()
