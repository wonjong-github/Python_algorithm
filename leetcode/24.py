# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapPairs(self, head:ListNode)->ListNode:
        """
        :type head: ListNode
        :rtype: ListNode
        """

        def go(node:ListNode)->ListNode:
            if not node:
                return None
            if not node.next:
                return node
            ret, ret.next, node = node.next, node, node.next.next
            ret.next.next = go(node)
            return ret

        return go(head)

arg1 = None
for n in [ 5, 4, 3, 2, 1]:
    temp = ListNode(n, None)
    arg1, arg1.next = temp, arg1
a = Solution()
a.swapPairs(arg1)