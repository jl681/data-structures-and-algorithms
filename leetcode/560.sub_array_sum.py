def sub_array_sum(nums, k):
    count = 0
    running_sum = 0
    sum_count = {0: 1}  # To handle the case where the sum itself is equal to k

    for num in nums:
        running_sum += num
        if running_sum - k in sum_count:
            count += sum_count[running_sum - k]

        # Update the count of the current running sum
        sum_count[running_sum] = sum_count.get(running_sum, 0) + 1

    return count


