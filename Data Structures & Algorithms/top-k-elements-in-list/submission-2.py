from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        top = defaultdict(int)
        mylist = []

        for i in nums:
            top[i] += 1

            if i not in mylist:
                mylist.append(i)

            j = mylist.index(i)

            while j > 0 and top[mylist[j]] > top[mylist[j - 1]]:
                mylist[j], mylist[j - 1] = mylist[j - 1], mylist[j]
                j -= 1

            if len(mylist) > k:
                mylist.pop()

        return mylist