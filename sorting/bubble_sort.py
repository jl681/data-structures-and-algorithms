
def bubble_sort(arr):
    n = len(arr)

    for i in range(n-1):

        swapped = False

        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        if not swapped:
            break

my_list = [6, 2, 7, 3, 5, 1, 4]
print(f"原始列表: {my_list}")

bubble_sort(my_list)  

print(f"排序后列表: {my_list}")


sorted_list = [1, 2, 3, 4, 5]
print(f"\n原始列表: {sorted_list}")
bubble_sort(sorted_list)
print(f"排序后列表: {sorted_list}") 
