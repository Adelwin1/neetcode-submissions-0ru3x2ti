class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next   

        
        second = slow.next
        slow.next = None

        prev = None
        while second:
            nextt = second.next
            second.next = prev
            prev = second
            second = nextt

        
        first = head
        secondt = prev

        while secondt:
            temp1 = first.next
            temp2 = secondt.next

            first.next = secondt
            secondt.next = temp1   

            first = temp1
            secondt = temp2        
