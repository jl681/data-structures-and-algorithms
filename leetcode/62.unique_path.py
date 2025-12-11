def unique_path(m, n):
    if m == 0 or n == 0:
        return 0
    if m == 1 or n == 1:
        return 1

    return unique_path(m - 1, n) + unique_path(m, n - 1)

print(unique_path(7, 3))