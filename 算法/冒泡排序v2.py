def bubble_sort(arr):
    for i in range(len(arr) - 1):
        pos = 0
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                pos = 1

        if pos == 0:
            break

    return arr


if __name__ == '__main__':
    arr = arr = [10, 8, 4, 7, 5]
    sort_arr = bubble_sort(arr)
    print(sort_arr)
