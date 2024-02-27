class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        y = ""
        
        if x[0] == '+' or x[0] == '-':
            if x[0] == '+':
                y += '+'
            else:
                y += '-'
                
            for i in range(len(x)-1, 0, -1):
                y += x[i]
                
        else:
            for i in range(len(x)-1, -1, -1):
                y += x[i]
                
        y = int(y)
        if y>2**31-1 or y<-2**31:
            return 0
        
        return y
