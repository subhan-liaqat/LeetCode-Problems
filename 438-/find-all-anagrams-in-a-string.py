class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p = sorted(p)
        k = len(p)
        res = []

        for i in range(len(s)-k+1): # ()0,7)
            windowStr = s[i:i+k] # 0:3
            if sorted(windowStr) == p:
                res.append(i)
        return res
