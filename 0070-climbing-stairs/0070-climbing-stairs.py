class Solution:
    def climbStairs(self, n: int) -> int:
        

        second_to_last = 1
        last = 1

        #we used _ as we are counting and i is not necessary
        for _ in range(n-1): 
            temp = second_to_last
            second_to_last = second_to_last + last
            last = temp
        
        return second_to_last


            