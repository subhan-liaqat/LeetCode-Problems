# Approach 1
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l <= r:
            sum = numbers[l] + numbers[r]

            if sum > target:
                r -= 1
            elif sum < target:
                l += 1
            else:
                return [l+1, r+1]


# Approach 1 (modified)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l <= r:
            sum = numbers[l] + numbers[r]

            if sum == target:
                return [l+1, r+1]
            elif sum > target:
                r -= 1
            elif sum < target:
                l += 1
