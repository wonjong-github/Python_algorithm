# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, l1:ListNode, l2:ListNode):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1


a = Solution()
arg1, arg2 = None, None
for n in [4, 2, 1]:
    temp = ListNode(n, None)
    arg1, arg1.next = temp, arg1
for n in [4, 3, 1]:
    temp = ListNode(n, None)
    arg2, arg2.next = temp, arg2
a.mergeTwoLists(arg1, arg2)