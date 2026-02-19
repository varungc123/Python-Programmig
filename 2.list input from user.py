l=[]
i=0
while(i<=4):
    print("enter the value")
    data=int(input())
    l.insert(i,data)
    i=i+1
print(l)
i=0
while(i<=4):
    if l[i]%2==0:
        print(l[i])
    i=i+1