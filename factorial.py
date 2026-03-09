def find_fact(n):
    if n <= 0:
        return 1
    return n*find_fact(n-1)
num=int(input("enter number : "))
res=find_fact(num)
print(f"the factorial of {num} is {res}")