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