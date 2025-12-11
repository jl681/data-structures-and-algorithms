def grid_travler_with_recursion(m, n):
    if m == 0 or n == 0: return 0
    if m == 1 or n == 1: return 1
    return grid_travler_with_recursion(m-1, n) + grid_travler_with_recursion(m, n-1)

def grid_travler_with_memoization(m,n, memo={}):
    key = str(m) + "," + str(n)
    if key in memo: return memo[key]
    if m == 0 or n == 0: return 0
    if m == 1 or n == 1: return 1

    memo[key] = grid_travler_with_memoization(m-1, n, memo) + grid_travler_with_memoization(m, n-1, memo)
    return memo[key]
