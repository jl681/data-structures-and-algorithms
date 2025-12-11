def selection_sort(arr):
    n = len(arr)

    for i in range(n-1):
        
        min_index = i

        for j in range(i,n-1):
            if arr[j] < arr[min_index]:
                min_index = j
        
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
        