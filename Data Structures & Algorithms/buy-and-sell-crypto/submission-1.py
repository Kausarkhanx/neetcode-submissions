class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # buy low sell high 
        # note - we can only sell after we buy the index

        # try 2 pointers approach 

        left = 0 
        right = 1
        max_profit = 0

        while right <= len(prices)-1:
            # right pointer value must always be GREATER than the left pointer value
            if prices[right]>prices[left]:
                #yes
                curr_profit = prices[right]-prices[left]
                max_profit = max(max_profit, curr_profit)
            else:
                #no
                left = right
            right = right+1
        return max_profit
