# Approach 1
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums+nums

# Approach 2
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in nums:
            ans.append(i)
        ans+=nums
        return ans

# Approach 3
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums
        ans.extend(nums)
        return ans
