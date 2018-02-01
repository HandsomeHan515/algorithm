def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) / 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    sort_arr = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sort_arr.append(left[i])
            i += 1
        else:
            sort_arr.append(right[j])
            j += 1

    print(sort_arr)

    sort_arr += left[i:]
    sort_arr += right[j:]
    return sort_arr


if __name__ == '__main__':
    arr = [10, 8, 4, 7, 5]
    sort_arr = merge_sort(arr)
    print(sort_arr)
