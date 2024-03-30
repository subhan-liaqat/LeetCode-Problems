class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = [] 
        # stack = empty
        # operation = D
        for operation in ops:
          if operation == '+':
            # to sum the previous values
            stack.append(stack[-1]+stack[-2])
          
          elif operation == 'C':
            stack.pop()
          
          elif operation == 'D':
            stack.append(2 * stack[-1] )
          
          else:
            stack.append(int(operation))
        
        return sum(stack)
