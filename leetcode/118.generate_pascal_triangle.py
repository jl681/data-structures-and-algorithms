def generate(numRows):
    if numRows == 1:
        return [[1]]
    result = []
    result[0] = [1]

    for i in range(1, numRows + 1):
        sub_array = list(range(1, i+1))
        result.append(sub_array)