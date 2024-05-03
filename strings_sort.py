def merge_sort_asc(items):
    if len(items) == 1:
        return items

    left = merge_sort_asc(items[0:len(items) // 2])
    right = merge_sort_asc(items[len(items) // 2:len(items)])

    result_array = [None] * len(items)
    l, r, i = 0, 0, 0

    while l < len(left) and r < len(right):
        if len(left[l]) <= len(right[r]):
            result_array[i] = left[l]
            l += 1
        else:
            result_array[i] = right[r]
            r += 1
        i += 1

    while l < len(left):
        result_array[i] = left[l]
        l += 1
        i += 1
    while r < len(right):
        result_array[i] = right[r]
        r += 1
        i += 1
    return result_array


def merge_sort_desc(items):
    if len(items) == 1:
        return items

    left = merge_sort_desc(items[0:len(items) // 2])
    right = merge_sort_desc(items[len(items) // 2:len(items)])

    result_array = [None] * len(items)
    l, r, i = 0, 0, 0

    while l < len(left) and r < len(right):
        if len(left[l]) >= len(right[r]):
            result_array[i] = left[l]
            l += 1
        else:
            result_array[i] = right[r]
            r += 1
        i += 1

    while l < len(left):
        result_array[i] = left[l]
        l += 1
        i += 1
    while r < len(right):
        result_array[i] = right[r]
        r += 1
        i += 1
    return result_array
