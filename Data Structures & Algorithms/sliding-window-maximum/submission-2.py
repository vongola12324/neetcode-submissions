class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window_max = []
        window = deque()

        for right in range(0, len(nums)):
            while len(window) > 0:
                if nums[window[-1]] < nums[right]:
                    window.pop()
                else:
                    break
            window.append(right)

            if right >= k - 1:
                while window[0] < right - k + 1:  # 過期條件
                    window.popleft()
                window_max.append(nums[window[0]])
        return window_max
