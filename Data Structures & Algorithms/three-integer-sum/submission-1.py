class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # [-1,0,1,2,-1,-4]
        # [-4, -1, -1, 0, 1, 2] # -4 + x = 0 , so x = 4
        output = []
        nums.sort()
        for index in range(len(nums)- 2):
            if index > 0:
                if nums[index] == nums[index - 1]:
                    continue
            left = index + 1
            right = len(nums) - 1
            while left < right:
                addition = nums[left] + nums[right]
                if addition + nums[index] == 0:
                    output.append([nums[index], nums[left], nums[right]])
                    # keep moving left and keep moving right until we dont find a duplicate
                    dupe1 = nums[left]
                    dupe2 = nums[right]
                    while nums[left] == dupe1 and left < right: # basically checking if nums ended:
                        left += 1
                    while nums[right] == dupe2 and right > left:
                        right -= 1
                elif addition + nums[index] < 0:
                    left += 1
                else:
                    right -= 1
        return output