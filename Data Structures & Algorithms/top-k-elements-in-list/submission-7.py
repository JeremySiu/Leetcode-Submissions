from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = defaultdict(int)
        for i in nums:
            num_freq[i] += 1
        
        bucket_sort = [[] for _ in range(len(nums))]

        for num, freq in num_freq.items():
            bucket_sort[freq - 1].append(num)
        
        res = []
        for i in range(len(bucket_sort) - 1, -1, -1):
            for j in bucket_sort[i]:
                if len(res) == k:
                    return res
                else:
                    res.append(j)
        return res