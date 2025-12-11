def longest_valid_parentheses(s):
    stack = [-1]  # Initialize the stack with -1 to handle edge cases
    max_length = 0

    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_length = max(max_length, i - stack[-1])

    return max_length

input_string = "(()())"
result = longest_valid_parentheses(input_string)
print(result)
