def comb(nums, outerList, innerList, target):
    # Base condition in recursion
    if target == 0:
        innerList.sort()
        if innerList in outerList:
            return
        outerList.append(innerList)
        return

    for i in range(len(nums)):
        if nums[i] > target:
            continue

        l = innerList.copy()
        l.append(nums[i])
        comb(nums, outerList, l, target-nums[i])
    return

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        outerList = [] # Lists are always pass by references whereas integers are pass by value
        innerList = []
        comb(candidates, outerList, innerList, target)
        return outerList
