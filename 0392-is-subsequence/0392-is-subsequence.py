# Approach 1
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == '':
            return True

        left = 0
        right = 0

        while left < len(s) and right < len(t):

            if s[left] == t[right]:
                left += 1

                if left == len(s):
                    return True
            right += 1
            
        return False


# Approach 2
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        index = 0
        length = len(s)

        if s == "":
            return True

        for i in t:

            if index < length:
                if i == s[index]:
                    index += 1

        if index == len(s):
            return True
            
        else:
            return False
