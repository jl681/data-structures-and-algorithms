def merge_sort(arr):
    """
    "总指挥" (分) - 归并排序的递归框架
    1. 分解 (Divide): 无脑对半砍
    2. 解决 (Conquer): 递归调用自己
    3. 合并 (Combine): 调用 merge 助手
    """
    
    # --- 1. 基准情况 (Base Case) ---
    # 这就是你说的 "最小单位"
    # 如果数组只有 1 个或 0 个元素，它天然就是有序的
    if len(arr) <= 1:
        return arr

    # --- 2. 分解 (Divide) ---
    # 无脑从正中间 "对半砍"
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # --- 3. 解决 (Conquer) ---
    # (信念之跃) 我相信 "merge_sort" (我自己)
    # 能分别把这两半排好序
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    # --- 4. 合并 (Combine) ---
    # "总指挥" 把两个排好序的子数组
    # 交给 "merge" 助手去干 "苦差事" (合并)
    return merge(sorted_left, sorted_right)


def merge(left, right):
    """
    "突击队长" (治) - 合并两个 "已排序" 的数组
    这正是消耗 O(n) 空间和 O(n) 时间的地方
    """
    
    # 1. 申请一个新数组 (这就是 O(n) 空间的来源)
    merged_array = []
    
    # 2. 设置两个 "指针"，分别指向两个数组的开头
    i = 0  # 指向 left
    j = 0  # 指向 right

    # 3. "挨个比较" 两个数组的元素
    while i < len(left) and j < len(right):
        # 谁小，谁就进入新数组
        if left[i] <= right[j]:
            merged_array.append(left[i])
            i += 1
        else:
            merged_array.append(right[j])
            j += 1

    # 4. 循环结束后，一个数组肯定 "掉出界" 了
    #    把另一个数组 "剩下" 的 (它们一定是最大的)
    #    全部复制到新数组末尾
    
    # 如果 left 剩下
    while i < len(left):
        merged_array.append(left[i])
        i += 1

    # 如果 right 剩下
    while j < len(right):
        merged_array.append(right[j])
        j += 1

    # 5. 返回这个 "合并" 好的、已排序的新数组
    return merged_array

# --- 示例 ---
my_array = [7, 2, 9, 1, 5, 3, 8]
print(f"Original array: {my_array}")

sorted_array = merge_sort(my_array)

print(f"Sorted array:   {sorted_array}")

# 另一个例子
my_array_2 = [3, -1, 5, 2, 0, 10, 4]
print(f"\nOriginal array: {my_array_2}")
print(f"Sorted array:   {merge_sort(my_array_2)}")