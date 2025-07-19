class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cs = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in cs:
                #if there is repetetion then you  remove values from left as long as the vlaue gets removed
                cs.remove(s[l])
                l = l + 1
            res = max(res, r - l + 1)
            cs.add(s[r])
        return res

        