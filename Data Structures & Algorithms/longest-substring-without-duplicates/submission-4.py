class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pos = {}
        left = 0
        max_length = 0

        for right, ch in enumerate(s):
            if ch in pos and pos[ch] >= left:
                left = pos[ch] + 1
            pos[ch] = right
            max_length = max(max_length, right - left + 1)

        return max_length


            
