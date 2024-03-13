class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()  # nums = [1, 4, 7, 9]
        l = 0
        r = k - 1

        minDiff = float('inf')
        while r < len(nums):  # 3 < 4
            minDiff = min(minDiff, nums[r] - nums[l])
            l += 1
            r += 1
        return minDiff