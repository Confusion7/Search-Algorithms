
#Use a linear search method to match the item in a list.

def search(array,key,n):
    for i in range(0,n):
        if key==array[i]:
            return i
            
    return -1
array=eval(input())
key=int(input())
array.sort()
n=len(array)
print(array)
result=search(array,key,n)
if result==-1:
    print("Element not found")
else:
    print("Element found at index: ",search(array,key,n))


