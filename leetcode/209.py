from typing import List

def min_subarray_len(target: int, nums: List[int]) -> int:
    left = 0
    min_len = float('inf') 
    current_count = 0
    
    for right in range(len(nums)):
        while current_count >= target:
            min_len = min(min_len,right - left+1)
            current_count -= nums[left] 
            left += 1
    return 0 if min_len == float('inf') else min_len
        