class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        temp = []
        for _ in range(len(self.stack)):
            temp.append(self.stack.pop())
        temp.append(x)
        for _ in range(len(temp)):
            self.stack.append(temp.pop())

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self.stack.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.stack[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.stack)==0
# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push("m")
obj.push("d")

param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()