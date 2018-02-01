def shell_sort(arr):
    gap = len(arr) // 2

    while gap > 0:
        for i in range(gap, len(arr)):
            while (i - gap) >= 0:
                if arr[i - gap] > arr[i]:
                    arr[i - gap], arr[i] = arr[i], arr[i - gap]
                    i -= gap
                else:
                    break
        gap = gap // 2

    return arr


if __name__ == '__main__':
    arr = [10, 8, 4, 7, 3]
    sort_arr = shell_sort(arr)
    print(sort_arr)
