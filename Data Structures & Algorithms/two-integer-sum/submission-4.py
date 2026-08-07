class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sol = defaultdict(int)
        for i, num in enumerate(nums):
            j = target - num 
            if j in sol:
                return [sol[j], i]
            else:
                sol[num] = i                
            