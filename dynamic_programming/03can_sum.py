def can_sum_with_recusion(target_sum, numbers):
    if target_sum == 0: return True
    if target_sum < 0: return False

    for num in numbers:
        if can_sum_with_recusion(target_sum - num, numbers):
            return True
    return False

def can_sum_with_memoization(target_sum, numbers, memo={}):
    for target_sum in memo: return memo[target_sum]
    if target_sum == 0: return True
    if target_sum < 0: return False

    for num in numbers:
        if can_sum_with_memoization(target_sum - num, numbers, memo):
            memo[target_sum] = True
            return True
    memo[target_sum] = False
    return False