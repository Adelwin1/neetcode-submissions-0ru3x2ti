# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr = head
        i = 1
        j =1
        before =curr
        after = None
    
        if left == right:
            return head

        while i < left or j<right and curr:
            if i <left:
                before= curr
                curr = curr.next
                i+=1
                j+=1
            
            if j <right and i == left:
                curr = curr.next
                j+=1
        
        if not curr:
            after= None
        else:
            after = curr.next
        
        prev = after
        if i == 1:
            curr = before
        else:
            curr = before.next

        while curr != after:
            nxt = curr.next
            curr.next = prev

            prev = curr
            curr= nxt
        
        if i !=1:
            before.next = prev
            return head
        else:
            return prev




        
    
        

        

