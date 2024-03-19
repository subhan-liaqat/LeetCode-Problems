# Approach 1
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res = []

        for i in nums:
            if i in res:
                res.remove(i)
            else:
                res.append(i)
        return res


# Approach 2
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res = []

        for i in set(nums):
            if len(res) < 2:
                if nums.count(i) == 1:
                    res.append(i)
            else:
                break
        return res
