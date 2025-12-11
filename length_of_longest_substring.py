
def length_of_longest_substring(arr):
    left = 0
    right = 0
    max_len = 0
    
    window = set()
    
    while right < len(arr):
        incoming = arr[right]
        
        while incoming in window:
            outgoing = arr[left]
            window.remove(outgoing)
            left += 1
            
        window.add(right)
        max_len = max(max_len, right - left + 1)
        right += 1
    
    return max_len

def length_of_longest_substring_optimized(s):
    left = 0
    max_len = 0
    
    # Map stores: { char : last_seen_index }
    char_map = {}
    
    for right in range(len(s)):
        incoming = s[right]
        
    
        if incoming in char_map and char_map[incoming] >= left:
            left = char_map[incoming] + 1
        
        char_map[incoming] = right
        
        # Update max_len
        max_len = max(max_len, right - left + 1)
        
    return max_len

    