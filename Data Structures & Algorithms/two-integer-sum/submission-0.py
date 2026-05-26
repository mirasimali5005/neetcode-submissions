class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # [4, 5, 6]
        # 6 not in so add 6,0 {6:0, 5:1, }
        # --
        # 6 in table so return 
        table = {}
        for i in range(len(nums)):
            if nums[i] not in table:
                table[target - nums[i]] = i
            else:
                return [table[nums[i]], i]
        