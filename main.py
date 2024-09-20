arr = [1, 3, 5, 6, 7, 8, 9, 10, 11]

def binaryRecursionSearch(arr, target, left, right):
    print(left, right)
    if left > right:
        return print('value does not found in the list')
    mid = (left + right) // 2
    if arr[mid] == target:
        binaryRecursionSearch(arr, target, mid + 1, right)
    elif arr[mid] > target:
        binaryRecursionSearch(arr, target, left, mid-1)


binaryRecursionSearch(arr, 99, 0, len(arr)-1)
binaryRecursionSearch(arr, 9, 0, len(arr)-1)
binaryRecursionSearch(arr, -1, 0, len(arr)-1)
