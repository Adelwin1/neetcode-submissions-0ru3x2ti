# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr= head
        l = 0

        while curr:
            curr= curr.next
            l+=1

        k = l-n
        i = 0
        curr = head
        dummy = curr
        prev = None
        while curr:
            if i!=k:
                i+=1
                prev = curr
                curr = curr.next
            else:
                if i ==0:
                    curr = curr.next
                    return curr
                else:
                    prev.next = curr.next
                    return dummy
        return dummy

            