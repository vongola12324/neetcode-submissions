class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        import heapq

        window_max = []
        window = []
        left = 0
        right = 0
        while right < len(nums):
            heapq.heappush(window, (-nums[right], right))

            if len(window) >= k:
                while left > window[0][1]:
                    heapq.heappop(window)
            
                window_max.append(-window[0][0])
                left += 1

            right += 1
        return window_max
