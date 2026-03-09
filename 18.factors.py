def factors(n,i):
    if i > n:
        return
    if n % i == 0:
        print(i,end=" ")
    factors(n,i+1)

n=int(input("enter number : "))
print(f"the factors of {n} is : " )
factors(n,1)
