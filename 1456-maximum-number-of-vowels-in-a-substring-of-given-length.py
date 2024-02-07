class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_vowels = curr = 0

        for i, char in enumerate(s):
            if (char in 'aeiou'):
                curr += 1
            if (i-k >= 0 and s[i - k] in 'aeiou'):
                curr -= 1
            max_vowels = max(max_vowels, curr)
        return max_vowels
