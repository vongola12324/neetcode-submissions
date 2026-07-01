class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        target_counter = defaultdict(int)
        for ch in t:
            target_counter[ch] += 1
        need = len(target_counter)  # 需要滿足幾個不同字元
        have = 0                     # 目前已滿足幾個
        answer = ""
        left = 0
        right = 0
        while right < len(s):
            # 加入右邊
            if s[right] in target_counter:
                target_counter[s[right]] -= 1
                if target_counter[s[right]] == 0:  # 剛好滿足這個字元
                    have += 1

            # 條件改成
            while have == need:
                if answer == "" or len(answer) > right - left + 1:
                    answer = s[left:right+1]
                # 收縮左邊
                if s[left] in target_counter:
                    if target_counter[s[left]] == 0:  # 即將不滿足這個字元
                        have -= 1
                    target_counter[s[left]] += 1
                left += 1
            right += 1
        return answer

        