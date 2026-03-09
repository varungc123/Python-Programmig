def findhcf(n1,n2):
    if n1 == 0:
        return n2
    if n1 < n2:
        n1,n2=n2,n1
    return findhcf((n1 % n2),n2)
def co_prime(n1,n2):
    if findhcf(n1,n2)==1:
        print("its coprime")
    else:
        print("not")
n1=int(input("enter the first number : "))
n2=int(input("enter the second number : "))
co_prime(n1,n2)