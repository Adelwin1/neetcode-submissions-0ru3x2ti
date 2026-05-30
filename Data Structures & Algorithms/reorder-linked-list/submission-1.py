class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        first = head
        dummy = first
        second = head

        while second and second.next:
            first = first.next
            second = second.next.next

        curr = first.next
        prev = None
        first.next = None

        while curr:
            nxt = curr.next
            curr.next = prev

            prev = curr
            curr = nxt

        while dummy and prev:
            temp = dummy.next
            temp2 = prev.next

            dummy.next = prev
            prev.next = temp

            dummy = temp
            prev = temp2