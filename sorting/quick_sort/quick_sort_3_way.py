def quick_sort_3_way(arr, low, high):
    """
    三路分区的 Quick Sort 实现。
    """
    if low >= high:
        return

    # 1. 设置三个指针
    lt = low       # 小于 pivot 区域的右边界
    gt = high      # 大于 pivot 区域的左边界
    i = low + 1    # 当前遍历的指针
    
    # 2. 选择 pivot (这里用 arr[low])
    pivot = arr[low]

    # 3. 当 i 还没有 "追上" gt 时
    while i <= gt:
        if arr[i] < pivot:
            # 交换到 "小于" 区域
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1
        elif arr[i] > pivot:
            # 交换到 "大于" 区域
            arr[gt], arr[i] = arr[i], arr[gt]
            gt -= 1
            # 注意：i 不增加，因为交换过来的 arr[i] 还没检查
        else: # arr[i] == pivot
            # 属于 "等于" 区域，i 直接右移
            i += 1

    # 4. 递归调用
    # 此时 [low...lt-1] 都是 < pivot
    # [lt...gt] 都是 == pivot (已排序)
    # [gt+1...high] 都是 > pivot
    
    # 递归排序 "小于" 部分
    quick_sort_3_way(arr, low, lt - 1)
    # 递归排序 "大于" 部分
    quick_sort_3_way(arr, gt + 1, high)

# --- 示例 ---
print("--- 3. Three-Way Partition ---")
# 使用一个有大量重复的数组来凸显优势
arr_3_way = [7, 2, 9, 1, 5, 3, 9, 5, 2, 7, 5]
print(f"Original: {arr_3_way}")
quick_sort_3_way(arr_3_way, 0, len(arr_3_way) - 1)
print(f"Sorted:   {arr_3_way}\n")