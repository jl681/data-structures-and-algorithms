# my solution
class Solution(object):
    def maximumWealth(self, accounts):
        max_wealth = 0
        for i in range(0, len(accounts)):
            current_wealth = 0
            for j in range(0, len(accounts[i])):
                current_wealth += accounts[i][j]
                if current_wealth >= max_wealth:
                    max_wealth = current_wealth
        return max_wealth

# another simplier solution
class Solution(object):
    def maximumWealth(self, accounts):
        return max(sum(array) for array in accounts)