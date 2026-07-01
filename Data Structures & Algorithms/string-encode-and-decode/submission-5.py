class Solution:
    SEPERATOR = "$"

    def encode(self, strs: List[str]) -> str:
        result = []
        for s in strs:
            result.append(f"{len(s)}{self.SEPERATOR}{s}")
        return "".join(result)

    def decode(self, s: str) -> List[str]:
        l = []
        parsing_begin_pos = 0
        current_pos = 0
        while current_pos < len(s):
            if s[current_pos] == self.SEPERATOR:
                parsing_length = int(s[parsing_begin_pos:current_pos])
                parsing_begin_pos = current_pos = current_pos + 1
                l.append(s[parsing_begin_pos:parsing_begin_pos+parsing_length])
                parsing_begin_pos = parsing_begin_pos+parsing_length
                current_pos += parsing_length
            else:
                current_pos += 1
        return l


