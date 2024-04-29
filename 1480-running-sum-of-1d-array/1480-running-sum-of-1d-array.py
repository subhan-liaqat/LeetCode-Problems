class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        run = 0 
        for i in range (len(nums)): 
            run += nums[i] 
            nums[i] = run
        return nums