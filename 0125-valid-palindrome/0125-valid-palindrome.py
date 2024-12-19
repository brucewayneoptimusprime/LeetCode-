class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and not self.alnum(s[l]):
                l = l + 1
            while r > l and not self.alnum(s[r]):
                r = r - 1

            if s[l].lower() != s[r].lower():
                 return False
                 
            else:
                l = l+1
                r = r-1
        return True
        
    def alnum(self, c):
          return (ord('A') <= ord(c) <= ord('Z') or
           ord('a') <= ord(c) <= ord('z') or
           ord('0') <= ord(c) <= ord('9') )



        
        

        