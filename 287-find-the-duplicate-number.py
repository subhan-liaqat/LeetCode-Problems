class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set() # [1, 3, 4, 2, 2]
        res = set() # [2]

        for i in nums:
            if i in seen:
                res.add(i)
            else:
                seen.add(i)
        return list(res)[0]
