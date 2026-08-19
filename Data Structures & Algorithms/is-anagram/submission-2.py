class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        letters = defaultdict(int)
        for i in s:
            letters[i] += 1
        for j in t:
            letters[j] -= 1
        for k in t:
            if letters[k] != 0:
                return False 
        return True
        