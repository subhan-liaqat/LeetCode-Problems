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