def fibonum(pos):
    if pos == 0 or pos == 1:
        return pos
    return fibonum(pos-1)+fibonum(pos-2)
pos=int(input("enter the position : "))
res=fibonum(pos)
print(f"the fibo num present at position: {pos} is {res}")