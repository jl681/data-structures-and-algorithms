def valid_palindrome(s):
    cleaned_s = ''.join(char.lower() for char in s if char.isalnum())
    left = 0
    right = len(cleaned_s) - 1
    
    while left < right:
        if(cleaned_s[left] != cleaned_s[right]):
            return False
        left += 1
        right -= 1
         
    return True

def is_palindrome(s):
    left = 0
    right = len(s) - 1
    
    while left < right:
        # Step 1: Move Left pointer forward until we find a letter/number
        # We must also check left < right to prevent going out of bounds
        while left < right and not s[left].isalnum():
            left += 1
            
        # Step 2: Move Right pointer backward until we find a letter/number
        while left < right and not s[right].isalnum():
            right -= 1
            
        # Step 3: Compare characters
        # We use .lower() to ignore case
        if s[left].lower() != s[right].lower():
            return False
            
        # Step 4: If match, move both inward
        left += 1
        right -= 1
        
    return True