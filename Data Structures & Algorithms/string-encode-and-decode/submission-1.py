class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for i in strs:
            encoded_str += f"{len(i)}#{i}"
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_str = []
        idx_start = 0
        idx_end = 0
        num = 0
        while idx_start < len(s):
            while s[idx_end] != '#':
                idx_end += 1
            num = int(s[idx_start:idx_end])
            idx_end += 1
            idx_start = idx_end
            idx_end += num
            decoded_str.append(s[idx_start:idx_end])
            idx_start = idx_end
        return decoded_str
            