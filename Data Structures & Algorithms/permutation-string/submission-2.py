class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        target = defaultdict(int)
        source = defaultdict(int)
        length = len(s1)
        for ch in s1:
            target[ch] += 1

        left = 0
        while left < length:
            source[s2[left]] += 1
            left += 1

        left = 0
        while left <= len(s2) - len(s1):
            # print(left, {ch: source[ch] for ch in source if source[ch] != 0})
            if all(target[ch] == source[ch] for ch in source if source[ch] != 0):
                return True
            if left+length >= len(s2):
                break
            source[s2[left]] -= 1
            # print(left, length, left+length)
            source[s2[left+length]] += 1
            left += 1

        return False

# 3
# 8
# ooooooxx