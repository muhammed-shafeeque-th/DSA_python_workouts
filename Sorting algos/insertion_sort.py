# Ascending order
def insertion_sort_ascending(arr: list) -> list:
    """
        Sort input list with insertion sort algorithm
            -- Time Complexity - O(n^2)
            -- Space Complexity - O(1)
    """
    # Sort in increasing order
    for i in range(1, len(arr)):
        curr = arr[i]
        j = i
        while j >= 1 and arr[j-1] > curr:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = curr

    return arr


# Descending order
def insertion_sort_descending(arr: list) -> list:
    """
        Sort input list with insertion sort algorithm Descending order
            -- Time Complexity - O(n^2)
            -- Space Complexity - O(1)
    """
    # Sort in increasing order
    for i in range(1, len(arr)):
        curr = arr[i]
        j = i
        while j >= 1 and arr[j-1] < curr:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = curr

    return arr

# Optimized method
def insertion_sort_with_reversed(arr: list, reversed=False) -> list:
    """
        Sort input list with insertion sort algorithm with reversed flag
            -- Time Complexity - O(n^2) - best case O(1)
            -- Space Complexity - O(1)
    """
    # insertion sort with reversed flag
    for i in range(1, len(arr)):
        curr = arr[i]
        j = i
        # Check if the reversed flag is true if =>
        if reversed:
            while j >= 1 and arr[j - 1] < curr:
                arr[j] = arr[j - 1]
                j -= 1
        else:
            while j >= 1 and arr[j - 1] > curr:
                arr[j] = arr[j - 1]
                j -= 1
        arr[j] = curr

    return arr



