n=int(input("enter the num"))
noc=n
for i in range(1,(2*n)):
    for k in range(n,noc,-1):
        print(" ",end="")
    for j in range(1,2*noc):
        print("* ",end="")
    print()
    if i<n:
        noc -= 1
    else:
        noc += 1