def three_sum(nums):
    nums.sort()
    result = []
    if not nums or len(nums) < 3:
        return result

    for i in range(len(nums) - 2):
        # after sorting this array, if the smallest number is beyond zero, then the result must be []
        if nums[i] > 0:
            break

        # 避免重复三元组,如果是[1,1,....]那么遍历到第一个和第二个得到的数组结果是一样的
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, len(nums) - 1

        # 双指针的break点在于两个不能遇到一起
        while left < right:
            target_sum = nums[i] + nums[left] + nums[right]
            if target_sum == 0:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif target_sum < 0:
                left += 1
            else:
                right -= 1

    return result

