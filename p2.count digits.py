n=int(input("enter number"))
count=0
while n>0:
    n=n//10     #eliminating last digit and updating it to n
    count=count+1  #counts +1  then repeat untill n>0
print(f"total digits of {n} is {count}")


#custom function
def countdigit(digi):
    count=0
    while digi>0:
        digi=digi//10
        count=count+1
    return count
digi=int(input("enter number"))                #insert  mkmmkkinput
res=countdigit(digi)                           #store output
print(f"digits of {digi} is : {res}")          #print output
