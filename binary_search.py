arr = [1,2,3,4,5,6,7,8]

x = 5

def binary_search(arr, l, r, x):
    if l > r:
        return -1
    
    mid = (l+r)//2

    if x < arr[mid]:
        return binary_search(arr, l, mid-1, x)

    elif x > arr[mid]:
        return binary_search(arr, mid+1, r, x)
    
    else:
        print(mid)
        return mid
    
found = binary_search(arr, 0, len(arr)-1, x)

if found == -1:
    print('not found')

else:
    print('found at ', found)