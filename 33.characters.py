n=int(input("enter the number"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(96+j),end=" ")
    print()

print("=============================")
for i in range(1,n+1):
    for j in range(n,i-1,-1):
        print(chr(96+j),end="")
    print()

print("=============================")
noc=4
for i in range(1,n*2):
    for j in range (1,noc):
        print(chr(96+j),end="")
    print()
    if i<n:
        noc+=1
    else:
        noc-=1

print("=============================")
noc=4
for i in range(1,n*2):
    for j in range (1,noc+1):
        print(chr(96+j),end="")
    print()
    if i<n:
        noc-=1
    else:
        noc+=1

print("=============================")
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(64+i),end=" ")
    print()


print("=============================")
for i in range(1,n+1):
    for j in range(1,i+1):
        if (i+j)%2==0 or i==j :
            print(chr(64+j),end=" ")
        else:
            print(chr(96+j),end=" ")
    print()

print("=============================")
for i in range(1,n+1):
    for j in range(n,i-1,-1):
        if j%2==0:
            print(chr(64+j),end=" ")
        else:
            print(chr(96+j),end=" ")
    print()

print("=============================")
for i in range(1,n+1):
    for j in range(1,n+1):
        if i%2==0:
            print(chr(64+j),end=" ")
        else:
            print(chr(96+j),end=" ")
    print()

print("=============================")
n=int(input("enter the number"))
count=1
for i in range(1,n+1):
    for j in range(0,n):
        print(chr(96+count),end=" ")
        if count<=26:
            count+=1
        else:
            count=1
    print()


print("=============================")
count=1
for i in range(1,n+1):
    for j in range(0,n):
        if j%2==1:
            print(chr(64+count),end=" ")
        else:
            print(chr(96+count),end=" ")
        if count<=26:
            count+=1
        else:
            count=1
    print()

print("=============================")
noc=1
for i in range(1,n*2):
    for j in range (1,noc+1):
        print(chr(64+i),end="")
    print()
    if i<n:
        noc+=1
    else:
        noc-=1

print("=============================")
for i in range(1,n+1):
    for j in range(n,i-1,-1):
        print(chr(96+j),end="")
    print()