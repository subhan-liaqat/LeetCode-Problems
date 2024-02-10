# Using sorted method, time complexity will be O(nlogn)
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


# Using hashmap, time complexity will be O(n)
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        res = []
        pCounter = Counter(p) # {a:1, b:1, c:1}
        windowCounter = Counter(s[:k]) # 0,1,2

        if pCounter == windowCounter:
            res.append(0)

        for i in range(len(s)-k):
            windowCounter[s[i]] -= 1

            if windowCounter[s[i]] == 0:
                del windowCounter[s[i]]

            windowCounter[s[i+k]] += 1

            if windowCounter == pCounter:
                res.append(i+1)

        return res
