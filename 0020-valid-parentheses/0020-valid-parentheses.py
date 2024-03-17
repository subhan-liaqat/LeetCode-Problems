class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            '(':')',
            '{':'}',
            '[':']'
        }
        stack = []

        for i in s:
            if i in brackets: # it's opening bracket
                stack.append(i)
            else: # it's closing bracket
                if not stack: return False
                b = stack.pop()
                if i != brackets[b]: return False

        return True if not stack else False               
