# First method
def selection_sort1(arr: list) -> list:
    """
        Sort input list with selection sort algorithm
            -- Time Complexity - O(n^2)
            -- Space Complexity - O(1)
    """
    # Sort in increasing order
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr


# Second method
def selection_sort2(arr: list) -> list:
    """
        Sort input list with selection sort algorithm
            -- Time Complexity - O(n^2)
            -- Space Complexity - O(1)
    """
    # Sort in decreasing order
    for i in range(len(arr) - 1):
        max_index = i
        for j in range(i + 1, len(arr)):
            if arr[max_index] < arr[j]:
                max_index = j  # find the max value index
        # place the max value in the correct position by swap
        arr[i], arr[max_index] = arr[max_index], arr[i]
    return arr


def selection_sort_with_reverse(arr: list, *, reversed=False) -> list:
    """
        Sort input list with selection sort algorithm
            -- Time Complexity - O(n^2)
            -- Space Complexity - O(1)
    """
    # Sort in decreasing order
    for i in range(len(arr) - 1):
        max_or_min_index = i
        for j in range(i + 1, len(arr)):
            if reversed:
                if arr[max_or_min_index] < arr[j]:
                    max_or_min_index = j  # find the max value index
            else:
                if arr[max_or_min_index] > arr[j]:
                    max_or_min_index = j  # find the min value index
        # place the max or min value in the correct position by swap
        arr[i], arr[max_or_min_index] = arr[max_or_min_index], arr[i]
    return arr


