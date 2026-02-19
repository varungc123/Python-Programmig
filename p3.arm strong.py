def countdigit(n):
    count=0
    while n>0:
        n=n//10
        count=count+1
    return count

n=(int(input("enter number")))
temp=n
pow=countdigit(n)
asn=0

while n>0:
    base=n%10                 #getting base that is last digit
    asn=asn+(base**pow)       #base powereed to pow
    n=n//10
if asn==temp:
    print(f"yes {temp} is a armstrong")
else:
    print(f"no {temp} is not a armstrong")