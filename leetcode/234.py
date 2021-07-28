# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import collections


class Solution(object):
    def isPalindrome(self, head)->bool:
        """
        :type head: ListNode
        :rtype: bool
        """
        # head_list = []
        # front = head
        # while front is not None:
        #     head_list.append(front)
        #     front = front.next
        #
        # return head_list == head_list[::-1]

        a, b, c = 6, 7, 8
        a, b, c = b, c, 1
        a = collections.deque()
        node = head
        while node is not None:
            a.append(node.val)
            node = node.next

        while len(a) > 1:
            if a.pop() != a.popleft():
                return False
        return True

a = Solution()
a.isPalindrome([1, 2, 2, 1])