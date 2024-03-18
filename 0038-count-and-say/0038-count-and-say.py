class Solution:
    def countAndSay(self, n: int) -> str:
        # base case
        if n == 1:
            return "1"
        
        prev = "1"
        end = n-1 

        for i in range(end): 

            result = ""  
            count = 1   
            digit = prev[0] 

            for j in range(1, len(prev)):
                
                if prev[j] == digit:
                    count += 1  
                else:
                    
                    result += str(count) + digit
                    count = 1  
                    digit = prev[j] 

            result += str(count) + digit
            prev = result  

        return prev