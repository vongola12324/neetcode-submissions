class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maxTotal = 0
        for item in nums:
            current = item
            currentTotal = 1
            while current - 1 in nums:
                current -= 1
                currentTotal += 1
            maxTotal = max(maxTotal, currentTotal)
        return maxTotal