"""
Merge Sort is a sorting algorithm based on the divide and conquer technique.

It:

- Divides the array into smaller halves

- Recursively sorts each half

- Merges the sorted halves back together
"""

mg = [8, 3, 5, 4, 7, 6, 1, 2]




def merge_sort(arr):
    """recursive split"""

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    # print(left)
    right = merge_sort(arr[mid:])
    # print(right)


    return merge(left, right)




def merge(left, right):
    """comparaison and sorting"""
    result = []
    i = j = 0

    # print(left, '  ', right)

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            # print(result)
            i +=1
        else: 
            result.append(right[j])
            # print(result)
            j += 1
        print(result)

    result.extend(left[i:])
    result.extend(right[j:])

    return result


# # here when we use [start:end] always return list
# last = mg[7:]
# print('last', last)


print(merge_sort(mg))
