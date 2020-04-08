def quick_sort(arr, left, right):

    if left >= right:
        return 

    pivot = arr[left]
    i = left
    j = right 

    while i < j:
        while j > i and arr[j] > pivot:
            j -= 1
        arr[i] = arr[j]
        while i < j and arr[i] <= pivot:
            i += 1
        arr[j] = arr[i]
    
    arr[i] = pivot
    quick_sort(arr, left, i)
    quick_sort(arr, i+1, right)

if __name__ == "__main__":
    arr = [7,5,1,3,6]
    quick_sort(arr, 0, len(arr)-1)
    print(arr)
    pass
    
        