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
        while start_pos < len(s):
            sep_pos = s.index(self.SEPERATOR, start_pos)
            if sep_pos == -1:
                break
            size = int(s[start_pos:sep_pos])
            tmp = s[sep_pos+1:sep_pos+1+size]
            l.append(tmp)
            start_pos = sep_pos+1+size

        return l


