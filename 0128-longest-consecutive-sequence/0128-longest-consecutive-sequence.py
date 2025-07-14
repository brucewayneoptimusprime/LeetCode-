class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for n in num_set:                # ← skip duplicates entirely
            if n - 1 not in num_set:     # n is the start of a run
                cur = n
                cur_len = 1
                while cur + 1 in num_set:
                    cur += 1
                    cur_len += 1
                longest = max(longest, cur_len)

        return longest
