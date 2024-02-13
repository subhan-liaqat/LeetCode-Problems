class Solution:
    def romanToInt(self, s: str) -> int:
        # create a hash table or dictionary to store values against roman numbers
        hash = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sum = 0
        length = len(s)

        for i in range(length):
            # need to check if there's next value after that
            # if there's any big value after small value like IV = 4 and VI = 6
            if i < (length - 1) and hash[s[i]] < hash[s[i+1]]:
                sum -= hash[s[i]]
            # add all values of roman numbers
            else:
                sum += hash[s[i]]
        return sum
