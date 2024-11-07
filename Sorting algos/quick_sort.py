def quick_sort(arr: list) -> list:
    """
    quick sort sorts array with divide and conquer approach
    -- Time complexity O(nlog n)
    -- Space complexity O(log n)
    :param arr:
    :return list:
    """
    # partition function which makes the arrangements and returns the partition place
    def partition(arr1: list, low: int, high: int) -> int:
        pivot = arr1[high]
        i = low - 1

        for j in range(low, high):
            if arr1[j] <= pivot:
                i += 1
                arr1[i], arr1[j] = arr1[j], arr1[i]
        arr1[i+1], arr1[high] = arr1[high], arr1[i+1]
        return i+1

    # [1, 54, 64, 55, 34, 21, 87, 98, 345, 67, 34, 343, 2, 23]

    def quick(arr2: list, low: int, high: int) -> None:
         if low < high:
            pvt_idx = partition(arr2, low, high)
            quick(arr2, low, pvt_idx-1)
            quick(arr2, pvt_idx + 1, high)

    quick(arr, 0, len(arr)-1)
    return arr


