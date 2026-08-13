class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        def area(height, width):
            return height * width 
        
        if len(heights) == 0:
            return 0

    
        mystack = Stack()
        i = 1
        answer = 0
        mystack.push(0)

        while i < len(heights) + 1:
            if i == len(heights):
                curr_height = 0
            else:
                curr_height = heights[i]

            if curr_height >= heights[mystack.peek()]:
                mystack.push(i)
            else:
                while mystack.is_empty() == False and curr_height < heights[mystack.peek()]:
                    pop = mystack.pop()
                    if mystack.peek() == None:
                        j = -1
                    else: 
                        j = mystack.peek()
                    height = heights[pop]
                    width = i - j - 1
                    cur_area = area(height, width)
                    if cur_area > answer: 
                        answer = cur_area

                if i != len(heights):
                    mystack.push(i) 
            i += 1

        return answer