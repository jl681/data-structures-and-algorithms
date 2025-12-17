
from typing import List

def remove_duplicate_from_sorted_arr(nums: List[int]) -> int:
    slow = 2
    
    for fast in range(2,len(nums)):
        if nums[fast] != nums[slow - 2]:
            nums[slow] = nums[fast]
            slow += 1
    return slow