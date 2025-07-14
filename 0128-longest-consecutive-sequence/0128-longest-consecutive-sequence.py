class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        x = set(nums)
        longest = 0

        for n in x:
            if (n-1) not in x:
                length = 1
                while (n + length) in x:
                    length = length + 1
                longest = max(length, longest)
        return longest

