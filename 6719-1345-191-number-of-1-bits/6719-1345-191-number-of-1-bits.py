class Solution:
    def hammingWeight(self, n: int) -> int:
        hamming_count = 0
        

        while n > 0:
            if n % 2 == 1:
                hamming_count = hamming_count + 1
            else:
                hamming_count = hamming_count + 0
            n = n >> 1
        return hamming_count


        