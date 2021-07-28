# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def oddEvenList(self, head:ListNode)->ListNode:
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        odd = head
        even = head.next
        even_first = head.next
        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
        odd.next = even_first
        return head

arg1 = None
for n in [ 5, 4, 3, 2, 1]:
    temp = ListNode(n, None)
    arg1, arg1.next = temp, arg1
a = Solution()
a.oddEvenList(arg1)
