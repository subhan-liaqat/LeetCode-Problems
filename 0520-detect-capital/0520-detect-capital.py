class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper():  # Agar saare characters capital hain
            return True
        elif word.islower():  # Agar saare characters lowercase hain
            return True
        elif word[0].isupper() and word[1:].islower():  # Agar sirf pehla character capital hai aur baaki lowercase hain
            return True
        else:
            return False