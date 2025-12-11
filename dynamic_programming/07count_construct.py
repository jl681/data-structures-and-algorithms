def count_construct_with_recursion(target, word_bank):
    if len(target) == 0 : return 1
    total_combination = 0
    for word in word_bank:
        if target.startswith(word):
            num_of_ways_for_rest = count_construct_with_recursion(target.replace(word, ""), word_bank)
            total_combination += num_of_ways_for_rest
    return total_combination

def count_construct_with_memoization(target, word_bank, memo = {}):
    if target in memo: return memo[target]
    if len(target) == 0 : return 1
    total_combination = 0
    for word in word_bank:
        if target.startswith(word):
            num_of_ways_for_rest = count_construct_with_memoization(target.replace(word, ""), word_bank)
            total_combination += num_of_ways_for_rest
    memo[target] = total_combination
    return total_combination
    

print(count_construct_with_recursion("purple", ["purp", "p", "ur", "le", "purpl"]))


