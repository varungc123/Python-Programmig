def count_digits(n,count):
    if n<=0:
        return count
    n=n//10
    count=count+1
    return count_digits(n,count)

def isarm(n,pow,asn,temp):
    if n<=0:
        return asnwhats
    base=n%10
    asn=asn+(base**pow)
    n=n//10
    return isarm(n,pow,asn,n)
n=int(input("enter num : "))
pow=count_digits(n,0)
print(pow)


