def lomuto_partition(arr, low, high):
    """
    Lomuto 分区实现。
    选择 arr[high] 作为 pivot。
    """
    # 1. 选择最后一个元素为 pivot
    pivot = arr[high]
    
    # 2. i 指针用来追踪 "小于 pivot" 区域的最后一个位置
    i = low - 1

    # 3. j 指针遍历从 low 到 high-1 的所有元素
    for j in range(low, high):
        # 4. 如果当前元素小于或等于 pivot
        if arr[j] <= pivot:
            # i 指针右移
            i += 1
            # 将这个小元素交换到 "小于 pivot" 区域的末尾
            arr[i], arr[j] = arr[j], arr[i]

    # 5. 遍历结束后，i 指向 "小于" 区域的最后一个元素
    #    将 pivot (arr[high]) 交换到 i+1 的位置
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    
    # 6. 返回 pivot 的最终位置
    return i + 1

def quick_sort_lomuto(arr, low, high):
    """Lomuto 分区的 Quick Sort 递归函数"""
    if low < high:
        # p 是 pivot 的索引
        p = lomuto_partition(arr, low, high)
        
        # 递归排序 pivot 左边的子数组
        quick_sort_lomuto(arr, low, p - 1)
        # 递归排序 pivot 右边的子数组
        quick_sort_lomuto(arr, p + 1, high)

# --- 示例 ---
print("--- 1. Lomuto Partition ---")
arr_lomuto = [7, 2, 9, 1, 5, 3, 9, 5]
print(f"Original: {arr_lomuto}")
quick_sort_lomuto(arr_lomuto, 0, len(arr_lomuto) - 1)
print(f"Sorted:   {arr_lomuto}\n")