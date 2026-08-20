class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sublist_ascii = defaultdict(list)
        for i in strs:
            key = [0 for _ in range(26)]
            for j in i:
                key[ord(j) - ord('a')] += 1
            sublist_ascii[tuple(key)].append(i)
        
        return list(sublist_ascii.values())