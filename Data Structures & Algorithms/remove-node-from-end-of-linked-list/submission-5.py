class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        slow = dummy
        fast = dummy

        # move fast n+1 steps ahead
        for _ in range(n + 1):
            fast = fast.next

        # move both until fast reaches end
        while fast:
            slow = slow.next
            fast = fast.next

        # remove node
        slow.next = slow.next.next

        return dummy.next

        
            