class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1 = 0
        prev2 = 0

        for n in nums:
            temp = prev1
            prev1 = max(n+prev2, prev1)
            prev2 = temp
        return prev1