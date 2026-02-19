def isprime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def printfactors(n):
    print("Factors:", end=" ")
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            print(i, end=" ")
            if i != n // i:  # paired factor
                print(n // i, end=" ")
    print()


num = int(input("Enter a number: "))

printfactors(num)

if isprime(num):
    print(num, "is prime")
else:
    print(num, "is not prime")
