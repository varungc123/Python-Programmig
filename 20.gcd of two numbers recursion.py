def check_gcd(n1,n2,i,hcf):
    if i > n1 or i > n2:
        return hcf
    if n1 % i == 0 and n2 % i == 0:
        hcf = i 
    return check_gcd(n1,n2,i+1,hcf)
n1=int(input("enter the first number : "))
n2=int(input("enter the second number : "))
ans=check_gcd(n1,n2,2,1)
print("gcd is ", ans)
#as the above code not working after certain number new efficient logic to be implemented(use euclidean algorithm......................