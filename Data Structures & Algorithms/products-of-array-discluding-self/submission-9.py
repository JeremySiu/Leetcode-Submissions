class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        post = 1
        output = [pre]
        for i in range(0, len(nums)-1):
            pre *= nums[i]
            output.append(pre)
        
        for i in range(len(nums)-1, -1, -1):
            output[i] *= post
            post *= nums[i]

        return output