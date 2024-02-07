# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA and headB:
            A, B = headA, headB
            while A != B:
                if A:
                    A = A.next
                else:
                    A = headB #If A reaches the end, reset it to the head of the other list (headB)
                if B:
                    B = B.next
                else:
                    B = headA #If B reaches the end, reset it to the head of the other list (headA)
            return B
