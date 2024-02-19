class Solution:
    def isNumber(self, s: str) -> bool:
        if s.replace('+', '').replace('-', '').isalpha():
            return False
        
        try:
            float(s)
            return True
        
        except:
            return False
