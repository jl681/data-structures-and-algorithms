from typing import List

def move_zeros(nums: List[int]) -> List[int]:
    slow = 0
    
    for fast in range(len(nums)):
        if nums[fast] != 0:
            # Swap the non-zero (fast) with the zero (slow)
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
    return nums

if __name__ == "__main__":
     result = move_zeros([0,1,0,3,12])
     print(result)