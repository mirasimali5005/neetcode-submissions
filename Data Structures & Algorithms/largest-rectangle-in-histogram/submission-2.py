class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # when something smaller comes we have to reset?
        # start something small came, measure it 
        # then
        # maybe prefix and suffix stack 
        # is it better to have the prefix or just stay put?
        # thats the case when at 5 and prefix is 1 so at 5
        # the answer stays 5
        # look left and right?
        # max height is already decided for each element all that remains is to see
        # when does that height become shorter from left and right and 
        # calculate the width of each 

        stack = [] # 0 
        # 1s max is till 0 
        # 4s max is till 1
        # 5s max is till 4 
        area = -1
        length = len(heights) - 1 # 5
        for index in range(len(heights)):
            if not stack:
                stack.append(index)
            else:
                while stack and heights[index] <= heights[stack[-1]]:
                    popped = stack.pop() # 0 
                    height = heights[popped] # 2
                    if stack:
                        width = index - stack[-1] - 1
                    else:
                        width = index # = 1
                    area = max(area, height*width)

                stack.append(index)
        
        while stack:
            index = stack.pop() # 4
            height = heights[index] # 2
            if stack:
                boundary = stack[-1]
                width = length - boundary # 4 
                area = max(area, width*height)
            else:
                # its the last element area is multiplied by length
                area = max(area, height * (length + 1))

        # for index in range(len(stack) - 1, 0, -1):
        #     width = length - index 
        #     area = width * height[index]

        return area