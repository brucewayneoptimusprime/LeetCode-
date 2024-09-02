class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closetotop = {"}" : "{", "]" : "[", ")" : "("}

        for c in s:
            if c in closetotop:
                if stack and stack[-1] == closetotop[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False
        