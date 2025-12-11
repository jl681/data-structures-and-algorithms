def insert(intervals, newInterval):
    if not newInterval:
        return intervals

    result = [intervals[0]]

    for i in range(len(intervals)):
        current_interval = intervals[i]
        if current_interval[0] <= newInterval[1] and current_interval[1] >= newInterval[0]:
            current_interval[0] = min(current_interval[0], newInterval[0])
            current_interval[1] = max(current_interval[1], newInterval[1])
        result.append(current_interval)
    return result

def insertInterval(intervals, newInterval):
    result = []
    i = 0
    n = len(intervals)

    # Add intervals that end before newInterval starts
    while i < n and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1

    # Merge overlapping intervals
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1

    # Add the merged interval to the result
    result.append(newInterval)

    # Add intervals that start after newInterval ends
    while i < n:
        result.append(intervals[i])
        i += 1

    return result





