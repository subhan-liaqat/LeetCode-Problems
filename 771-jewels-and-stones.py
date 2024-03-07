# Approach 1
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stoneBox = {}
        noOfJewels = 0

        for s in stones:
            if s not in stoneBox:
                stoneBox[s] = 1
            else:
                stoneBox[s] += 1

        for j in jewels:
            if j in stoneBox:
                noOfJewels += stoneBox[j]

        return noOfJewels


  # Approach 2
  class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for i in stones:
            for j in jewels:
                if i == j:
                    count += 1
        return count

        
# Approach 3
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for i in stones:
            if i in jewels:
                count += 1
        return count


# Approach 4
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = 0
        for i in jewels:
            counter += stones.count(i)
        return counter
