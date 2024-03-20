class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        max_lenght = 0
        visited = set()

        for index,value in enumerate(nums): # 0 - > 5
            current_length = 0
            # visited_set = {0,2,5,6} # 4

            while value not in visited:
                current_length += 1
                visited.add(value) 
                value = nums[value] # 2

            if max_lenght < current_length:
                max_lenght = current_length
        return max_lenght
