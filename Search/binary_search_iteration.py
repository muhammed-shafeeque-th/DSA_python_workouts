
def binary_search(arr: list, value: int) -> int:
    """
    -Accepts a sorted array returns the position of the value
    -Returns -1 if the value is not found.
    -- Time complexity O(log n)
    -- space complexity O(1)
     """
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if value == arr[mid]:
            return mid
        elif value < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return -1


