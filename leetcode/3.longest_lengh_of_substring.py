def longest_length_of_substring(s):
    if not s or len(s) == 0:
        return 0

    start_index, max_length, char_index_map = 0, 0, {}
    for end, char in enumerate(s):
        if char in char_index_map and char_index_map[char] >= start_index:
            start_index = char_index_map[char] + 1

        char_index_map[char] = end
        current_length = end - start_index + 1
        max_length = max(max_length, current_length)
    return max_length
