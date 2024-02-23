# Approach 1
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] = digits[i] + 1
                return digits
        return [1] + digits


# Approach 2
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        # Convert array into string
        res = ""
        for i in digits:
            res += str(i)

        # Convert string into integer to add once and then again convert to string
        res = int(res) + 1
        res = str(res)

        # Convert string into array
        arr = []
        for i in res:
            arr+=[int(i)]

        return arr
