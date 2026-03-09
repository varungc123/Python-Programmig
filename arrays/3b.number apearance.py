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
target=int(input("enter target number"))

def appearance(arr,target):
    count=0
    for i in range(0,len(arr)):
        if arr[i]==target:
            count+=1
    return count
res=appearance(arr,target)
print(res)