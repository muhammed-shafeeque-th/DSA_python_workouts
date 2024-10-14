# First method
def bubble_sort(arr: list) -> list:
    """
        Sort input list with bubble sort algorithm
            -- Time Complexity - O(n^2)
            -- Space Complexity - O(1)
    """
    # Sort in increasing order
    for i in range(len(arr)):
        for j in range(1, len(arr) - i):
            if arr[j-1] > arr[j]:
                arr[j], arr[j-1] = arr[j-1], arr[j]

    return arr


# Optimized method
def optimized_bubble_sort(arr: list) -> list:
    """
        Sort input list with bubble sort algorithm with optimized method
            -- Time Complexity - O(n^2) - best case O(1)
            -- Space Complexity - O(1)
    """
    # Bubble sort in optimized way
    for i in range(len(arr)):
        swapped = False  # Flag to check whether values have swapped or not
        for j in range(1, len(arr) - i):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j - 1]
                swapped = True
        # if the arr is not swapped in any iteration of j means array is sorted
        if not swapped:
            break
    return arr


# Optimized method
def optimized_bubble_sort_with_reversed(arr: list, reversed=False) -> list:
    """
        Sort input list with bubble sort algorithm with reversed flag in optimized method
            -- Time Complexity - O(n^2) - best case O(1)
            -- Space Complexity - O(1)
    """
    # Bubble sort in optimized way order
    for i in range(len(arr)):
        swapped = False
        for j in range(1, len(arr) - i):
            if reversed:
                if arr[j-1] < arr[j]:
                    arr[j-1], arr[j] = arr[j], arr[j-1]  # swap values
                    swapped = True  # set values are swapped at least once
            else:
                if arr[j - 1] > arr[j]:
                    arr[j - 1], arr[j] = arr[j], arr[j - 1]  # swap values
                    swapped = True  # set values are swapped at least once
        # if the arr is not swapped at least once in iteration of j means array is sorted
        if not swapped:
            break
    return arr



