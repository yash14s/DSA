arr = [1,3,2,10,5,2]

def merge_sort(arr, s, e):
    print("merge_sort(",arr,s,e,")")

    #base case
    if e-s+1 <= 1:
        return arr
    
    m = (s+e)//2

    print("left")
    merge_sort(arr, s, m) #left
    print("right")
    merge_sort(arr, m+1, e) #right

    merge(arr, s, m, e)

    return arr


def merge(arr, s, m, e):
    print("merge(",s,m,e,")")
    l = arr[s:m+1]
    r = arr[m+1:e+1]

    i = 0
    j = 0
    k = s

    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            arr[k] = l[i]
            i += 1
        else:
            arr[k] = r[j]
            j += 1
        k += 1

    while i < len(l):
        arr[k] = l[i]
        i += 1
        k += 1

    while j < len(r):
        arr[k] = r[j]
        j += 1
        k += 1


sorted = merge_sort(arr, 0, len(arr)-1)
print(sorted)