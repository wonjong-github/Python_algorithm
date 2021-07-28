# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1: ListNode, l2: ListNode)->ListNode:
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = 0
        index = 0
        while l1 is not None:
            num1 = (10**index)*l1.val + num1
            l1 = l1.next
            index+=1

        num2 = 0
        index = 0
        while l2 is not None:
            num2 = (10 ** index) * l2.val + num2
            l2 = l2.next
            index += 1

        num1 += num2

        def go(num:int):
            if not num1:
                return ListNode(0, None)
            if not num:
                return None
            ret = ListNode(num%10, None)
            ret.next = go(num//10)
            return ret

        return go(num1)

a = Solution()
arg1, arg2 = None, None
for n in [4, 2, 1]:
    temp = ListNode(n, None)
    arg1, arg1.next = temp, arg1
for n in [4, 3, 1]:
    temp = ListNode(n, None)
    arg2, arg2.next = temp, arg2
a.addTwoNumbers(arg1, arg2)