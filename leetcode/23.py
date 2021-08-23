# Definition for singly-linked list.
import heapq


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeKLists(self, lists:list[ListNode])->ListNode:
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        answer = node = ListNode()
        heap = []
        for i in lists:
            heapq.heappush()
