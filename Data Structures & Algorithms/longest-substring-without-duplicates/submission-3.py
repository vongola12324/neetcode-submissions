class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        pos = {s[0]: 0}
        left = 0
        right = 1
        max_length = 0
        while right < len(s):
            if s[right] in pos:
                next_left = pos[s[right]] + 1
                for ch in s[left:next_left]:
                    del pos[ch]
                left = next_left
            pos[s[right]] = right
            max_length = max(max_length, len(pos))
            right += 1
        return max_length


            
