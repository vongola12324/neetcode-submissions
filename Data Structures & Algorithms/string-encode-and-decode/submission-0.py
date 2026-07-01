class Solution:
    SEPERATOR = "$"

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += f"{len(s)}{self.SEPERATOR}{s}"
        print(result)
        return result

    def decode(self, s: str) -> List[str]:
        l = []
        start_pos = 0
        while start_pos < len(s):
            sep_pos = s[start_pos:].index(self.SEPERATOR)
            if sep_pos == -1:
                break
            size = int(s[start_pos:start_pos+sep_pos])
            tmp = s[start_pos+sep_pos+1:start_pos+sep_pos+1+size]
            l.append(tmp)
            start_pos = start_pos+sep_pos+1+size

        return l


