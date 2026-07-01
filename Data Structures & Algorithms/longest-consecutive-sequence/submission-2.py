class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maxTotal = 0
        for item in nums:
            currentTotal = 1
            if item - 1 not in s:
                nxt = item + 1
                while nxt in s:
                    nxt += 1
                    currentTotal += 1
            maxTotal = max(maxTotal, currentTotal)
        return maxTotal