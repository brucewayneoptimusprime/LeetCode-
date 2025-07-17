class Solution:
    def countBits(self, n: int) -> List[int]:
        #we will begin by creating the dp array
        dp = [0] * (n+1)
        #the array is initialized with the specified size in question and with all zeros
        #we use offset because n as in our explanation is already used for naming the integer parameter in ques
        offset_value = 1


        # we also don't wish to begin at 0 as 0 has no 1s and it is no that relevant to the sequence
        for i in range(1, n+1):
            if offset_value * 2 == i:
                offset_value = i
            dp[i] = 1 + dp[i - offset_value]
        return dp

        