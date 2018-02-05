def binary_search(key, array):
    low = 0
    high = len(array) - 1

    while(low <= high):
        middle = (low + high) // 2
        if key == array[middle]:
            return middle
        elif key < array[middle]:
            high = middle - 1
        else:
            low = middle + 1

    return None


if __name__ == '__main__':
    arr = [1, 3, 4, 5, 7, 9]
    search = binary_search(3, arr)
    print('search: {}'.format(search))
