class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero = 0
        counter = 0
        while counter < len(nums) - 1:
            if nums[counter] == 0:
                zero += 1
                counter += 1
            else:
                break
        prod = nums[counter]
        for i in range(counter + 1, len(nums)):
            if nums[i] == 0:
                zero += 1
            else:
                prod *= nums[i]
        
        res = []
        for i in nums:
            if (i != 0 and zero > 0) or (i == 0 and zero > 1):
                res.append(0)
            elif i == 0 and zero == 1:
                res.append(int(prod))
            else:
                res.append(int(prod/i))

        return res