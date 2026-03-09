def createIntarray():
    print(" enter the numbers to array")
    arr=[]
    while True:
        try:
            n=int(input(" enter the number : "))
            arr.append(n)
        except ValueError:
            return arr
        except Exception as e:
            return arr
arr=createIntarray()
print("created array",arr)

sum=0
product=0
for i in range(0,len[arr]):
    sum=arr[i]+arr[i+1]
    product=arr[i]+arr[i+1]
    i+=2