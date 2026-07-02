class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """

        # Create set
        obstaclesSet = set()
        for x, y in obstacles:
            obstaclesSet.add((x,y))

        # North, East, South, West
        direction = [(0,1), (1,0), (0,-1), (-1,0)]
        x, y, currDir, answer = 0, 0, 0, 0

        for command in commands:

            # Check for turns
            if command == -1:
                currDir = (currDir + 1) % 4
            elif command == -2:
                currDir = (currDir + 3) % 4
            else:
                for i in range(command):
                    
                    # add new step
                    newX = x + direction[currDir][0]
                    newY = y + direction[currDir][1]

                    # check if obstical blocks it
                    if (newX, newY) in obstaclesSet:
                        break
                    x, y = newX, newY

                    answer = max(answer, x**2 + y **2)

        return answer