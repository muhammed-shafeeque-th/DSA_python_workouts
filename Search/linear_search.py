
def linear_search(arr: list, value: int) -> int:
    """
    -Accepts and array, returns the position of the value
    -Returns -1 if the value is not found.
    -- Time complexity O(n)
    -- Space complexity O(1)
     """
    for idx in range(len(arr)):
        if arr[idx] == value:  # check the array element and target value are the same
            return idx  # returns index of the array element

    return -1  # return -1 if the value does not exist in array

