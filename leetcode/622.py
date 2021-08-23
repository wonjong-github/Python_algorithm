import collections


class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.queue = collections.deque
        self.start = self.last = 0
        self.size = 0

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if len(self.queue) >= self.size:
            return False
        self.queue.append(value)
        return True

    def deQueue(self):
        """
        :rtype: bool
        """
        if len(self.queue) == 0:
            return False
        self.queue.popleft()
        return True

    def Front(self):
        """
        :rtype: int
        """
        return self.queue[0]

    def Rear(self):
        """
        :rtype: int
        """
        return self.queue[-1]

    def isEmpty(self):
        """
        :rtype: bool
        """
        return len(self.queue) == 0

    def isFull(self):
        """
        :rtype: bool
        """
        return len(self.queue) == self.size

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

t = collections.deque
len(t)