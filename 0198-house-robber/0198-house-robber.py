class Solution:
    def rob(self, nums: List[int]) -> int:
        memory_one_back = 0
        memory_two_back = 0

        for n in nums:
            temp = max(n + memory_two_back, memory_one_back)
            memory_two_back = memory_one_back
            memory_one_back = temp
        return memory_one_back
        