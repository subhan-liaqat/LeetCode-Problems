class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        n, m = len(nums1), len(nums2)
        removals = n + m - k
        ranks1 = self.find_ranks(nums1)
        ranks2 = self.find_ranks(nums2)

        max_removals_nums1 = min(removals, n)
        min_removals_nums1 = removals - min(removals, m)
        out = self.getOutput(nums1, nums2, max_removals_nums1, removals, ranks1, ranks2)
        removals_nums1 = max_removals_nums1 - 1
        while removals_nums1 >= min_removals_nums1:
            out_t = self.getOutput(nums1, nums2, removals_nums1, removals, ranks1, ranks2)
            out = self.getMax(out, out_t)
            removals_nums1 -= 1
        return out
        
    def find_ranks(self, nums):
        n = len(nums)
        ranks, moving_rank, st = [0] * n, 0, [0]
        for i in range(1, n):
            while len(st) > 0 and nums[st[-1]] < nums[i]:
                e = st.pop()
                ranks[e] = n - moving_rank
                moving_rank += 1
            st.append(i)
        while st:
            e = st.pop()
            ranks[e] = n - moving_rank
            moving_rank += 1
        return ranks

    def getMax(self, out1, out2):
        for i in range(len(out1)):
            if out1[i] > out2[i]:
                return out1
            if out2[i] > out1[i]:
                return out2
        return out1

    def getOutput(self, nums1, nums2, removals_nums1, removals, ranks1, ranks2):
        removals_nums2 = removals - removals_nums1
        nums1_f = self.getFilteredN(nums1, removals_nums1, ranks1)
        nums2_f = self.getFilteredN(nums2, removals_nums2, ranks2)

        i, j = 0, 0
        out = []
        while i < len(nums1_f) and j < len(nums2_f):
            if nums1_f[i] > nums2_f[j] or (nums1_f[i] == nums2_f[j] and self.isFirstBigger(nums1_f[i:], nums2_f[j:])):
                out.append(nums1_f[i])
                i += 1
            else:
                out.append(nums2_f[j])
                j += 1

        while i < len(nums1_f):
            out.append(nums1_f[i])
            i += 1

        while j < len(nums2_f):
            out.append(nums2_f[j])
            j += 1

        return out

    def getFilteredN(self, nums, toRemove, ranks):
        toKeep = len(nums) - toRemove
        out = []
        for i in range(len(ranks)):
            if ranks[i] <= toKeep:
                out.append(nums[i])
        
        return out

    def isFirstBigger(self, nums1, nums2):
        com = min(len(nums1), len(nums2))
        for i in range(com):
            if nums1[i] > nums2[i]:
                return True
            if nums2[i] > nums1[i]:
                return False

        return len(nums1) > len(nums2)