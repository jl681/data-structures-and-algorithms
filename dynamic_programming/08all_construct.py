def all_construct_with_recursion(target, word_bank):
    if len(target) == 0: return [[]]
     
    all_combinations = []
    for word in word_bank:
        if target.startswith(word):
            result_list = all_construct_with_recursion(target.replace(word,""), word_bank)
            for result in result_list:
                result.append(word)
            all_combinations += result_list
    return all_combinations

def all_construct_with_memoization(target, word_bank, memo={}):
    if target in memo: return memo[target]
    if len(target) == 0: return [[]]
    all_combinations = []
    for word in word_bank:
        if target.startswith(word):
            result_list = all_construct_with_memoization(target.replace(word,""), word_bank, memo)
            for result in result_list:
                result.append(word)
            all_combinations += result_list
    memo[target] = all_combinations
    return all_combinations
        

print(all_construct_with_recursion("purple", ["purp", "p", "ur", "le", "purpl"]))


