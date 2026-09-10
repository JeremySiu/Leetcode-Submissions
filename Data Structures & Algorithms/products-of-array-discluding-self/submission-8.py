class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        zero_counter = 0
        init_prod = self.calculateProduct(nums, 0)
        res = [init_prod]
        for i in range(1, len(nums)):
            if nums[i] == 0:
                zero_counter += 1
                if nums[0] == 0 or zero_counter > 1:
                    res.append(0)
                else:
                    res.append(int(self.calculateProduct(nums, i)))
            else:
                init_prod = int(init_prod * nums[i-1] / nums[i])
                res.append(init_prod)
        return res

    def calculateProduct(self, nums, i):
        prod = 1
        for j in range(0, len(nums)):
            if j == i:
                continue
            else:
                prod *= nums[j]
        return prod
            