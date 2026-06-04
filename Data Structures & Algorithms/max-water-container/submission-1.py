class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # when the sides are the same i need to figure the logic 
        
        # before keep moving from the smaller side

        front = 0 
        back = len(heights) - 1 # 7
        max_area = 0
        while front < back:
            area = min(heights[front], heights[back]) * (back-front)
            max_area = max(area, max_area)
            if heights[front] < heights[back]:
                front += 1
            elif heights[front] > heights[back]:
                back -= 1
            else:
                # both are the bottle necks i dont think we need to check which height is smaller
                # any would work properly 
                if heights[front + 1] < heights[back - 1]:
                    front += 1
                else:
                    back -= 1
        return max_area