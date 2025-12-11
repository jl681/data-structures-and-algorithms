def how_sum_with_recursion(target_sum, numbers):
    if target_sum == 0: return []
    if target_sum < 0: return None

    for num in numbers:
        result = how_sum_with_recursion(target_sum - num, numbers)
        if result != None:
            result += [num]
            return result
      
    return None

def how_sum_with_memoization(target_sum, numbers, memo={}):
    for target_sum in memo: return memo[target_sum]
    if target_sum == 0: return []
    if target_sum < 0: return None

    for num in numbers:
        result = how_sum_with_memoization(target_sum - num, numbers, memo)
        if result != None:
            result += [num]
            memo[target_sum] = result
            return result
    memo[target_sum] = None
    return None