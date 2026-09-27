class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = [asteroids[0]]

        for i in range(1, len(asteroids)):
            

            asteroid = asteroids[i]

            if (asteroid < 0 and stack[-1] > 0) or (asteroid > 0 and stack[-1] < 0):
                if (abs(stack[-1]) > abs(asteroid)):
                    continue
                elif (abs(stack[-1]) < abs(asteroid)):
                    stack.pop()
                elif abs(stack[-1]) == abs(asteroid):
                    stack.pop()
            else:
                stack.append(asteroid)

        return list(stack)
                