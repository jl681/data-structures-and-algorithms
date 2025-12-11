def four_sum_count(nums1, nums2, nums3, nums4):

    result_map = {}

    for num1 in nums1:
        for num2 in nums2:
            result_map[num1 + num2] = result_map.get(num1 + num2, 0) + 1

    count = 0
    for num3 in nums3:
        for num4 in nums4:
            complement = -(num3 + num4)
            if complement in result_map:
                count += result_map[complement]

    return count

