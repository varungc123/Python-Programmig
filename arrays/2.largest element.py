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

def largest(arr):
    largest = arr[]
    index = -1
    for i in range(0,len(arr)):
        if arr[i] > largest:
            largest = arr[i]
            index = i
    return largest,index

res,resindex = largest(arr)

print("Largest element:", res)
print("First occurrence index:", resindex)