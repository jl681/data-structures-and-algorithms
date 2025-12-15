
def longgest_repeating_character_replacement(s, k):
    left = 0
    replacement_count = 0
    
    for right in range(1,len(s)):
        if(s[right] != s[right-1]):
            s[right] = s[right-1]
            replacement_count += 1
        if replacement_count > k:
            if s[left] != s[right]:
                replacement_count -= 1
            left += 1
    return right - left + 1
    