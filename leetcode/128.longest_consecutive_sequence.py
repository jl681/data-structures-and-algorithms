def longest_consecutive(nums):
    nums.sort()
    result_map = {}
    max_length = 0
    for num in nums:
        current_length = 1
        if num - 1 in result_map:
            current_length += result_map[num - 1]
        result_map[num] = current_length
        max_length = max(current_length, max_length)
    return max_length


# 实际上以从小到大的遍历取代了排序
def longest_consecutive_without_sorting(nums):
    if not nums:
        return 0
    nums_set = set(nums)
    longest_streak = 0
    for num in nums:

        # 这里是取代排序的关键
        if num - 1 not in nums_set:
            current_streak = 1
            current_num = num

            while current_num + 1 in nums_set:
                current_num += 1
                current_streak += 1
            longest_streak = max(longest_streak, current_streak)
    return longest_streak


def longest_consecutive_with_hash(nums):
    result_map = {}
    max_streak = 0
    for num in nums:
        if num not in result_map:
            left = result_map.get(num - 1, 0)
            right = result_map.get(num + 1, 0)
            current_streak = right + left + 1
            max_streak = max(max_streak, current_streak)
            result_map[num], result_map[num - left], result_map[num + right] = (current_streak, current_streak,
                                                                                current_streak)
    return max_streak

print(longest_consecutive_with_hash(([100,4,200,1,3,2])))




