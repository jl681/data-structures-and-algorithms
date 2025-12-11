def remove_element(nums, val):
    j = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[j] = nums[i]
            j += 1
    return j, nums

def remove_element_01(nums, val):
    j = 0
    for i in range(len(nums)):
        if nums[i] != val:
            if i > j:
                nums[j] = nums[i]
            j +=1
    return j, nums
    