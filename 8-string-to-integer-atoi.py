class Solution:
    def myAtoi(self, s: str) -> int:
        # remove whitespaces from start and end
        s = s.strip()
        if not s:
            return 0

        sign = 1
        # if first element in negative then sign = -1 otherwise 1
        if s[0] == '+' or s[0] == '-':
            if s[0] == '-':
                sign = -1
            s = s[1:]
        
        num = 0
        for char in s:
            # if there's any alphabetical value
            if not char.isdigit():
                break
            #if there's integer value
            else:
                num = (num * 10) + int(char)
        
        num *= sign

        # number should not be more than 2^31 - 1 or less than -2^31
        num = max(min(num, 2**31 - 1), -2**31)
        return num
