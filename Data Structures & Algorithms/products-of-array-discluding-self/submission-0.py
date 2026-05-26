class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[1], nums[0]]
        suffix = [nums[-1], nums[-2]]
        pre = nums[1] * nums[0]
        suf = nums[-1] * nums[-2]
        for i in range(2, len(nums)):
            prefix.append(pre)
            pre = pre*nums[i]
        for i in range(len(nums) - 3, -1, -1):
            suffix = [suf] + suffix
            suf = suf*nums[i]
        for i in range(1, len(suffix)-1):
            suffix[i] *= prefix[i]
        suffix[-1] = prefix[-1]
        return suffix
        
        
        

