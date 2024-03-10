class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')': '(',  '}': '{', ']': '['}
        pointer = 0
        while 0 < pointer+1 < len(s):
            if s[pointer+1] in brackets:
                if s[pointer] != brackets[s[pointer+1]]:
                    return False
                s = s[:pointer] + s[pointer+2:]
                pointer -= 1 if pointer > 0 else pointer
                continue
            pointer += 1
        return not s