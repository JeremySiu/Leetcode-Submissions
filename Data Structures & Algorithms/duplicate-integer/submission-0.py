class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        onlyNums = []
        for i in nums:
            if i in onlyNums:
                return True
            else:
                onlyNums.append(i)
        return False