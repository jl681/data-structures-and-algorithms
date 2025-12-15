from typing import List

def max_consecutive_ones_iii(arr, k):
    left = 0
    zero_count = 0
    
    for right in range(len(arr)):
        
        if(arr[right] == 0):
            zero_count += 1
        if zero_count > k:
            if arr[left] == 0:
                zero_count -= 1
            left += 1
               
    return len(arr) - left

def longest_ones(nums: List[int], k: int) -> int:
    left = 0
    max_len = 0
    zeros = 0
    
    for right in range(len(nums)):
        if nums[right] == 0:
            zeros += 1
            
        while zeros > k:
            if nums[left] == 0:
                zeros -= 1
            left += 1

        max_len = max(max_len, right - left + 1)
        
    return max_len
            