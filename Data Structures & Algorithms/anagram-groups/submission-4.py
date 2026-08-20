class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sublist_ascii = defaultdict(int)
        anagrams = []
        idx_counter = 0
        for i in strs:
            ascii_key = self.createKey(i)
            if ascii_key in sublist_ascii:
                anagrams[sublist_ascii[ascii_key]].append(i)
            else:
                sublist_ascii[ascii_key] = idx_counter
                anagrams.append([])
                anagrams[idx_counter].append(i)
                idx_counter += 1
        return anagrams


    def createKey(self, string):
        key = [0 for _ in range(26)]
        for i in string:
            key[ord(i)-ord('a')] += 1
        return tuple(key)