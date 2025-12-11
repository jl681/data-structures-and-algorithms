def climb_stairs_with_recursive(n):
    if n == 2:
        return 2
    if n == 1:
        return 1
    return climb_stairs_with_recursive(n - 2) + climb_stairs_with_recursive(n - 1)


def climb_stairs_with_memoization(n, result_map= {}):
    if n in result_map:
        return result_map[n]
    if n == 2:
        return 2
    if n == 1:
        return 1
    result_map[n] = climb_stairs_with_recursive(n - 2, result_map) + climb_stairs_with_recursive(n - 1, result_map)
    return result_map[n]

def climb_stairs_with_tabulation(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    result = [0] * (len(n) + 1)
    result[1] = 1
    result[2] = 2

    for i in range(3, n + 1):
        result[i] = result[i - 1] + result[i - 2]
    return result[n]


