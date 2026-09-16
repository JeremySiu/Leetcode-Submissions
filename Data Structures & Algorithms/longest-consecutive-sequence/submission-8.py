class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        longest_consec = 0
        while len(my_set) > 0:
            i = my_set.pop()
            max_num = i + 1
            min_num = i - 1
            current_consec = 1
            while max_num in my_set:
                my_set.discard(max_num)
                max_num += 1
                current_consec += 1
            while min_num in my_set:
                my_set.discard(min_num)
                min_num -= 1
                current_consec += 1
            longest_consec = max(current_consec, longest_consec)
        return longest_consec