class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        target_counter = defaultdict(int)
        for ch in t:
            target_counter[ch] += 1
        answer = ""
        left = 0
        right = 0
        while right < len(s):
            if s[right] in target_counter:
                target_counter[s[right]] -= 1
            
            while all(count <= 0 for count in target_counter.values()):
                # 用 while 持續收縮，直到不滿足為止
                if len(answer) > right - left + 1 or answer == "":
                    answer = s[left:right+1]
                if s[left] in target_counter:
                    target_counter[s[left]] += 1
                left += 1
            
            right += 1  # 外層統一推進
        return answer

        