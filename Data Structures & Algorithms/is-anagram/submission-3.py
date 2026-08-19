class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_letters = defaultdict(int)
        t_letters = defaultdict(int)
        for i in s:
            s_letters[i] += 1
        for j in t:
            t_letters[j] += 1
        if s_letters == t_letters:
            return True
        return False