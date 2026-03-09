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
target=int(input("enter the target"))


def linearsearch(arr,target):
    for i in range(0,len(arr)):
        if arr[i]==target:
            return True, i
    return False,-1

flag,index=linearsearch(arr,target)

if flag:
    print(f"the {target} element is fount at :{index}")
else:
    print("not found")

