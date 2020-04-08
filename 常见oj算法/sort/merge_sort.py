def divide(arr, left, right):

    if left >= right:
        return 
    
    mid = (left+right)//2

    divide(arr, left, mid)
    divide(arr, mid+1, right)

    merge(arr, left, right)

def merge(arr, left, right):

    mid = (left+right)//2

    left_arr = arr[left:mid+1]
    right_arr = arr[mid+1:right+1]
    print(left_arr, right_arr)
    il, ir = 0, 0

    for i in range(left, right+1):
        if il < len(left_arr) and ir < len(right_arr):
            if left_arr[il] < right_arr[ir]:
                arr[i] = left_arr[il]
                il += 1
            else:
                arr[i] = right_arr[ir]
                ir += 1
        elif il < len(left_arr):
            arr[i] = left_arr[il]
            il += 1
        elif ir < len(right_arr):
            arr[i] = right_arr[ir]
            ir += 1

if __name__ == "__main__":
    arr = [2,3,1,7,4,10,15]
    divide(arr, 0, len(arr)-1)
    print(arr)
    pass