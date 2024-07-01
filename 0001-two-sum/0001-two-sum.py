class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hash_table ={}

        for index, num in enumerate(nums):

            complement = target - num

            if complement in hash_table:

                return([hash_table[complement], index])
            
            else:
                hash_table[num] = index
        