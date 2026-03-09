def createinarry():
    print(" enter value to arrays")
    arr=[]
    while True:
        try:
            if len[arr]<2:
                n=input(" enter string now ")
                arr.append(n)
        except ValueError as e:
            return arr
        except Exception as e:
            return arr
arr=createinarry()
print("created ",arr)