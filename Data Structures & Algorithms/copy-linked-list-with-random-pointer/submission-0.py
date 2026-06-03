class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        copies = {}

        curr = head
        while curr:
            copies[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            copy = copies[curr]

            copy.next = copies.get(curr.next)
            copy.random = copies.get(curr.random)

            curr = curr.next

        return copies[head]