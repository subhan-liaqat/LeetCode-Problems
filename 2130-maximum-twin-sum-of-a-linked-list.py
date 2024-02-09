# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        # Convert Linked List to an Array
        value = []
        curr = head
        while curr:
            value.append(curr.val)
            curr = curr.next
        
        # value = [5, 4, 2, 1]
        i = 0
        j = len(value) - 1
        max_sum = 0

        while i <= j:
            max_sum = max(max_sum, value[i] + value[j])
            i += 1
            j -= 1
        return max_sum
