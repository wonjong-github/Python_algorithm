# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head: ListNode)->ListNode:
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # answer = None
        #
        # while head is not None:
        #     answer, answer.next, head = head, answer, head.next
        # return answer

        node, prev = head, None
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        return prev

arg1 = None
for n in [5, 4, 3, 2, 1]:
    temp = ListNode(n, None)
    arg1, arg1.next = temp, arg1
a = Solution()
a.reverseList(arg1)

a = ''.join(map(str, [5, 4, 3, 2, 1]))
print(type(a))