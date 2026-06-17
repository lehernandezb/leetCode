class Solution(object):
    
    # Good solution and worked on first attempt. Things to make it better, we actually dont need tuple for this. 
    # We just need indexs for this to make it space time o(1)
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        array = [(key, i) for i, key in enumerate(height, 1)]

        found = 0
        headptr = 0
        tailptr = len(height) - 1

        while headptr <= tailptr:
            y = array[headptr][0] if array[headptr][0] < array[tailptr][0] else array[tailptr][0]
            x = abs(array[headptr][1] - array[tailptr][1])
            area = x*y
            if area > found:
                  found = area
                  print(y, x)
            
            if array[headptr][0] > array[tailptr][0]:
                  tailptr -= 1
            else:
                  headptr += 1
        return found
                  