def hoare_partition(arr, low, high):
    """
    Hoare 分区实现。
    选择 arr[low] 作为 pivot。
    """
    # 1. 选择第一个元素为 pivot
    pivot = arr[low]
    
    # 2. i 和 j 指针分别在数组范围之外开始
    i = low - 1
    j = high + 1

    while True:
        # 3. i 指针向右移动，直到找到 >= pivot 的元素
        while True:
            i += 1
            if arr[i] >= pivot:
                break
        
        # 4. j 指针向左移动，直到找到 <= pivot 的元素
        while True:
            j -= 1
            if arr[j] <= pivot:
                break

        # 5. 如果 i 和 j 交错，说明本轮分区结束
        if i >= j:
            # 注意：Hoare 返回的是 j (分界点)
            # 并不一定是 pivot 元素所在的索引！
            return j

        # 6. 如果 i 还在 j 左边，交换它们
        arr[i], arr[j] = arr[j], arr[i]

def quick_sort_hoare(arr, low, high):
    """Hoare 分区的 Quick Sort 递归函数"""
    if low < high:
        # p 是分界点 (split point)
        p = hoare_partition(arr, low, high)
        
        # 递归排序左半部分 (low 到 p)
        # 注意这里是 p，不是 p - 1
        quick_sort_hoare(arr, low, p)
        # 递归排序右半部分 (p + 1 到 high)
        quick_sort_hoare(arr, p + 1, high)

# --- 示例 ---
print("--- 2. Hoare Partition ---")
arr_hoare = [7, 2, 9, 1, 5, 3, 9, 5]
print(f"Original: {arr_hoare}")
quick_sort_hoare(arr_hoare, 0, len(arr_hoare) - 1)
print(f"Sorted:   {arr_hoare}\n")