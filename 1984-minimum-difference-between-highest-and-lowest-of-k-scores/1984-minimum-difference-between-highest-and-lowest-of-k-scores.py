# Approach 1
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:

        nums.sort()
        size = k - 1
        minDiff = float('inf')

        for i in range(len(nums)):
            
            if i >= size : # window has started 
                low = nums[i - size]
                high = nums[i]
                minDiff = min(minDiff, high - low)

        return minDiff


# Approach 2
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
