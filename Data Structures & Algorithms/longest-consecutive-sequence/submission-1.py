class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maxTotal = 0
        for item in nums:
            current = item
            currentTotal = 1
            if current - 1 not in s:
                current += 1
                while current in s:
                    current += 1
                    currentTotal += 1
            maxTotal = max(maxTotal, currentTotal)
        return maxTotal