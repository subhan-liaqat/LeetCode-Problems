class Solution:
    # @staticMethod
    def reverseLinkedList(self, begin: Optional[ListNode], end: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while begin != end:
            next = begin.next
            begin.next = prev
            prev = begin
            begin = next

        return prev


    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1 or head is None or head.next is None:
            return head
        
        dummy = ListNode(0, head)
        back, forward = dummy, head

        while back is not None:
            groupLen = 0
            while groupLen < k and forward is not None:
                forward = forward.next
                groupLen += 1
            
            if groupLen != k:
                break
            
            last = back.next

            back.next = self.reverseLinkedList(back.next, forward)
            
            last.next = forward
            back = last

        return dummy.next