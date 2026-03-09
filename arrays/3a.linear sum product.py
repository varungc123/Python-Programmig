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

def sumprod(arr):
    sum=0
    prod=1
    for i in range(0,len(arr)):
        sum=sum+arr[i]
        prod=prod*arr[i]
    return sum,prod
res1,res2=sumprod(arr)
print(f"the sum of {arr} is {res1} and product of {arr} is {res2}")

