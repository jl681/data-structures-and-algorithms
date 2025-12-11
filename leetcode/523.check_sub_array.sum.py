# 我的错误的做法
def check_sub_array_sum(nums, k):

    running_sum = 0
    result = {0: True}

    for num in nums:
        running_sum += num
        if running_sum % k in result:
            return True
        result[running_sum] = True

    return result.get(0, False)


# chatgpt的做法
def checkSubarraySum(nums, k):
    prefix_sum = 0
    sum_mod_k = {0: -1}  # To handle the case where a subarray starts from the beginning

    for i, num in enumerate(nums):
        prefix_sum += num
        if k != 0:
            prefix_sum %= k

        if prefix_sum in sum_mod_k:
            if i - sum_mod_k[prefix_sum] > 1:
                return True
        else:
            sum_mod_k[prefix_sum] = i

    return False

# 为什么这个例子应该返回true
print(checkSubarraySum([5,0,0,0], 3))
