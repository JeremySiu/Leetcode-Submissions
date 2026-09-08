from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = defaultdict(int)
        for i in nums:
            num_freq[i] += 1
        
        arr = []
        for num, freq in num_freq.items():
            arr.append([freq, num])
        arr.sort()

        return_list = []
        while len(return_list) < k:
            return_list.append(arr.pop()[1])

        return return_list
        