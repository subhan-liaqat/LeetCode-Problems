class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashSet = []
        for i in nums:
            if i in hashSet:
                return True
            else:
                hashSet.append(i)