class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        intersect = list(set(nums1) & set(nums2))

        if intersect:
            return sorted(intersect)[0]
        else:
            return -1
