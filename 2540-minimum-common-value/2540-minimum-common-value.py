# Approach 1
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i = 0
        j = 0
        common = float('inf')

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                common = nums1[i]
                break
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        
        return common if common != float('inf') else -1


# Approach 2
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        intersect = list(set(nums1) & set(nums2))

        if intersect:
            return sorted(intersect)[0]
        else:
            return -1
