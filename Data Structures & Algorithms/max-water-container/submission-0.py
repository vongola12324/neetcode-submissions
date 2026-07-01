class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxTotal = 0
        left = 0
        right = len(heights) - 1
        while left < right < len(heights):
            currentTotal = min(heights[left], heights[right]) * (right - left)
            # print(left, right, currentTotal)
            maxTotal = max(maxTotal, currentTotal)
            if heights[right] > heights[left]:
                left += 1
            else:
                right -= 1
        return maxTotal

            