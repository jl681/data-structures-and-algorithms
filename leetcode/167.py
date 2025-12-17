from typing import List


def two_sum_ii(nums: List[int], target: int) -> List[int]:
    
    left = 0
    right = len(nums) - 1
    
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left+1, right+1]
        if current_sum < target:
            left += 1
        if current_sum > target:
            right -= 1
    
    return []