# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        # If the entire list had the specified value, return None
        if not head:
            return None

        # Skip leading nodes with the specified value
        while head and head.val == val:
            head = head.next

        # Iterate through the rest of the list to remove nodes with the specified value
        temp = head
        while temp:
            if temp.next and temp.next.val == val:
                temp.next = temp.next.next
            else:
                temp = temp.next

        return head
