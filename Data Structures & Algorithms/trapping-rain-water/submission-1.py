class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        wall = []
        water = []
        right = 1
        for i, h in enumerate(height):
            if h > 0:
                wall.append(h)
                water.append(0)
                right = i + 1
                break
        while right < len(height):
            if height[right] >= wall[0]:
                total += sum(water) + sum(wall[0]-w for w in wall)
                wall = [height[right]]
                water = [0]
            else:
                tmp = []
                while height[right] > wall[-1]:
                    last_wall = wall.pop()
                    last_water = water.pop()
                    min_wall = min(height[right], wall[0])
                    tmp.append((min_wall, last_water+min_wall-last_wall))
                while len(tmp) != 0:
                    last = tmp.pop()
                    wall.append(last[0])
                    water.append(last[1])
                wall.append(height[right])
                water.append(0)
            right += 1
        total += sum(water)

        return total