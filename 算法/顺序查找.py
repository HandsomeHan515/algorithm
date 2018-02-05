def order_search(key, array):
    length = len(array)
    if array == None or not length:
        return "key 不存在"

    for i in range(length):
        if (array[i] == key):
            return i

    return "key 不存在"


if __name__ == '__main__':
    arr = [1, 3, 4]
    search = order_search(10, arr)
    print('search: {}'.format(search))
