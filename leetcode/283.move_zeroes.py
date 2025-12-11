def move_zeroes(nums):
    j = 0
    for i in range(len(nums)):
        if nums[i]:
            nums[j] = nums[i]
            j += 1
    for i in range(j, len(nums)):
        nums[i] = 0

def move_zeroes_1(nums):
    j = 0
    for i in range(len(nums)):
        if nums[i]:
            if i > j:
                nums[j] = nums[i]
                nums[i]= 0
            j += 1
