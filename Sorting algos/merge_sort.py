def merge_sort(arr: list) -> list:
    """
        Sort input list with quick sort algorithm
            -- Time Complexity - O(nlog n)
            -- Space Complexity - O(log n)
    """
    def _merge_sort(arr1: list) -> list:
        if len(arr1) <= 1:
            return arr1

        mid = len(arr1) // 2
        sorted_left = _merge_sort(arr1[:mid])
        sorted_right = _merge_sort(arr1[mid:])

        return _merge(sorted_left, sorted_right)

    def _merge(srtd_left: list, srtd_right: list) -> list:
        result = []
        i = j = 0
        while i < len(srtd_left) and j < len(srtd_right):
            if srtd_left[i] < srtd_right[j]:
                result.append(srtd_left[i])
                i += 1
            else:
                result.append(srtd_right[j])
                j += 1
        result.extend(srtd_right[j:])
        result.extend(srtd_left[i:])
        return result

    return _merge_sort(arr)