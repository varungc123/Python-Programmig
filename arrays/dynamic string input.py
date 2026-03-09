def createStrtarry():
    print(" enter value to arrays")
    arr=[]
    while True:
        n=input("enter the string ")
        if n=="":
            return arr
        arr.append(n)

arr=createStrtarry()
print("created ",arr)