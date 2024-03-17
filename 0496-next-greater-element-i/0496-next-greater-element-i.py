# Approach 1 - Optimal
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        ans = defaultdict(lambda: -1)  # if there's no key then return -1 as default dictionary
        stack = []

        # create a dictionary and store next greater element as a value using stack 
        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                ans[stack.pop()] = nums2[i]
            stack.append(nums2[i])

        # replace the integers in nums1 with values of ans dictionary
        for i in range(len(nums1)):
            nums1[i] = ans[nums1[i]]
        return nums1


# Approach 2
