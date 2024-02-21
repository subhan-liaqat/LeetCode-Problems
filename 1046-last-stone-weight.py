class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones) > 1:
            stones.sort() # [1, 1, 2, 4, 7, 8]

            x = stones.pop()
            y = stones.pop()

            stones.append(abs(x-y))

        return stones[0] if stones else 0
