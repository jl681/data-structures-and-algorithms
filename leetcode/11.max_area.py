def max_area(height):

    area = 0
    for i in range(len(height)):
        for j in range(i, len(height)):
            area = max(min(height[i], height[j]) * (j - i), area)
    return area

def max_area_01(height):

    max_area = 0
    j = len(height) - 1    
    i = 0

    while(i < j):
        max_area = max(min(height[i], height[j]) * (j - i), max_area)
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return max_area

print(max_area_01([1,8,6,2,5,4,8,3,7]))


