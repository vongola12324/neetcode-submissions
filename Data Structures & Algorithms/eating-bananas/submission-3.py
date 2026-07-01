class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        left = 1
        right = max(piles)
        while left < right:
            mid = (left+right-1) // 2
            total_hours = sum(math.ceil(p / mid) for p in piles)
            if total_hours <= h:
                right = mid
            else:
                left = mid + 1
        return left

"""
sum(ceil(p / k) for p in piles) < h
312884470
968709470
"""