def fibo(pos):
    n1 = 0  #starting of fibo will always be 0 and 1
    n2 = 1
    while (pos>0):
        print(n1,end=" ")   #printing first number
        temp=n1+n2  #adding and storing
        n1=n2       #n1 is n2
        n2=temp     #added temp  is n2
        pos -= 1    #decrement and repeat
pos=int(input("enter number position"))
fibo(pos)

#decrementing for loop
def fibo1(pos1):
    n1 = 0  #starting of fibo will always be 0 and 1
    n2 = 1
    for pos1 in range(pos1,0):
        print(n1,end=" ")   #printing first number
        temp=n1+n2  #adding and storing
        n1=n2       #n1 is n2
        n2=temp     #added temp  is n2
        pos -= 1    #decrement and repeat
pos1=int(input("\nenter number position"))
fibo1(pos1)
