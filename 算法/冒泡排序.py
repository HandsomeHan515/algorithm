def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


                
if __name__ == '__main__':
    arr = [10, 8, 4, 7, 5]
    sort_arr = bubble_sort(arr)
    print(sort_arr)
    
# 排序过程   
# [8, 4, 7, 5, 10]
# [4, 7, 5, 8, 10]
# [4, 5, 7, 8, 10]
# [4, 5, 7, 8, 10]
