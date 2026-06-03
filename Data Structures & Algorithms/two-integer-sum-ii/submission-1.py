class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # [1, 2, 3, 4]
        #  ^        ^ 3 - 4 = -1
        #  ^     ^ 3 - 3 = 0
        #  ^  ^ 3 - 2 = 1

        # [2, 3, 6, 8] # 14
        #  ^.       ^ 14-8 = 6
        #.    ^.    ^. 14 - 8 = 
        
        front = 0
        back = len(numbers) - 1
        while numbers[back] + numbers[front] != target:
            diff = target - numbers[back]
            if diff < numbers[front]:
                back -= 1
            elif diff > numbers[front]:
                front += 1
        return [front + 1, back + 1]