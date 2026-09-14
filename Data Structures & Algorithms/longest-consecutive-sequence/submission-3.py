class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        if len(nums) == 0:
            return 0
        longest_consec = 1
        while len(my_set) > 0:
            i = my_set.pop()
            max = i + 1
            min = i - 1
            current_consec = 1
            while max in my_set:
                my_set.discard(max)
                max += 1
                current_consec += 1
            while min in my_set:
                my_set.discard(min)
                min -= 1
                current_consec += 1
            if current_consec > longest_consec:
                longest_consec = current_consec
        return longest_consec