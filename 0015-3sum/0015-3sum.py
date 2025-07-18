class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result_array = []
        nums.sort()

        for i, a in enumerate(nums):
            #To avoid repetetion of first element
            if i > 0 and a == nums[i-1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                if (a + nums[l] + nums[r] > 0):
                    r = r - 1
                elif (a + nums[l] + nums[r] < 0):
                    l = l + 1
                else:
                    result_array.append([a,nums[l],nums[r]])
                    l = l + 1 #To try remaining permutations
                    while l < r and nums[l] == nums[l-1]:
                        l = l + 1 #To try to avoid repetetion of the second element
                        
        return result_array
            
                 

        