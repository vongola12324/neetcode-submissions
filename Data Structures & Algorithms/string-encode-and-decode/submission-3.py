class Solution:
    SEPERATOR = "$"

    def encode(self, strs: List[str]) -> str:
        result = []
        for s in strs:
            result.append(f"{len(s)}{self.SEPERATOR}{s}")
        return "".join(result)

    def decode(self, s: str) -> List[str]:
        l = []
        start_pos = 0
        need_size = -1
        start_pos = 0
        index = 0
        while index < len(s):
            if s[index] == self.SEPERATOR:
                need_size = int(s[start_pos:index])
                start_pos = index = index + 1
                if need_size == 0:
                    l.append("")
                else:
                    l.append(s[start_pos:start_pos+need_size])
                start_pos = start_pos+need_size
                index += need_size
                need_size = -1
            else:
                index += 1
        return l


