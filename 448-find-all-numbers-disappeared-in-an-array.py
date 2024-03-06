class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = set(nums)
        missing = []

        for i in range(len(nums)):
            if i not in res:
                missing.append(i)

        return missing
