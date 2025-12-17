def longest_repeating_character(s, k):
    left = 0
    counts = {}
    max_fre = 0
    max_len = 0
    
    for right in range(len(s)):
        current_char = s[right]
        counts[current_char] =  counts.get(current_char, 0) + 1
        max_fre = max(max_fre, counts[current_char])
        
        while right - left + 1 - max_fre > k:
            left_char = s[left]
            counts[left_char] -= 1
            left += 1
        max_len = max(max_len,right - left + 1)
    return max_len
        
    