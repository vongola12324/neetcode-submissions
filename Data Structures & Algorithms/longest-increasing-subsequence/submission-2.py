class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0]*2001
        for num in nums:
            prev = 0
            if num > -1000:
                prev = max(dp[:num+1000])
            dp[num+1000] = prev + 1
        return max(dp)
