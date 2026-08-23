class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for i in strs:
            encoded_string += " "
            for j in i:
                encoded_string += f"{ord(j)}" + "+"
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        num = ""
        for i in s:
            if i == '+':
                decoded_strs[-1] += chr(int(num))
                num = ""
            elif i == ' ':
                decoded_strs.append("")
            else:
                num += i
        return decoded_strs 
