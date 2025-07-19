class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # (length of window) - (element having maximum frequency [within a hashmap]) <= k
        freq = {}
        max_length = 0

        l = 0
        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0)

            while (r - l + 1) - (max(freq.values())) > k:
                freq[s[l]] = freq[s[l]] - 1
                l = l + 1
            
            max_length = max(max_length, r - l + 1)
        return max_length