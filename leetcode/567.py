from typing import Counter


def permutation_in_string(s1, s2):
    if len(s1) > len(s2):
            return False
        
    target_counter = Counter(s1)
    window_size = len(s1)
    left = 0
    
    for left in range(len(s2) - window_size + 1):
        current_counter = Counter(s2[left : left + window_size])
        if target_counter == current_counter:
            return True
            
    return False


def check_in_clusion(s1: str, s2: str) -> bool:
    n1, n2 = len(s1), len(s2)
    if n1 > n2: return False

    s1_counts = Counter(s1)
    window_counts = Counter(s2[:n1]) # Initialize with the first window
    
    # Check the first window immediately
    if s1_counts == window_counts:
        return True

    # Slide the window across the rest of s2
    for i in range(n1, n2):
        new_char = s2[i]          # The char entering from the right
        old_char = s2[i - n1]     # The char leaving from the left
        
        # 1. Update the window count in O(1)
        window_counts[new_char] += 1
        window_counts[old_char] -= 1
        
        # 2. Clean up to keep the map small
        if window_counts[old_char] == 0:
            del window_counts[old_char]
            
        # 3. Check equality in O(26)
        if s1_counts == window_counts:
            return True
            
    return False