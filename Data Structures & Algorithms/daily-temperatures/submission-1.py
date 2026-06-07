class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack approach
        # last element is always 0 
        # and if there is one element return [0]
        # keep a stack and keep popping until you find element bigger?

        # 28 = 0
        # 28 40 -> 40
        # 35 # 40 so 1 is the answer
        # 35 40 
        # 36 # 35 40 1 pop used 
        # so now it will be 36 40
        # 30 # 36 40 so now its also one 
        # 30 36 40 # it should be in order because if not then the 
        # bigger one is already before it 
        # now 38 
        # pop 30 and 36 so now we would have # 38 40 and answer is 2
        # since we had to pop twice
        # we can keep track of jumps(indices maybe) of how much it take
        # to get to a bigger number?


        stack = [] # [1, 3, 4]
        output = [0]*len(temperatures) # [1, 0, 1, 0, 0, 0, 0, 0, 0]
        for TempInt in range(len(temperatures)): # 4
            if not stack:
                stack.append(TempInt)
            else:
                # start a loop to see all the elements temp is bigger
                # than
                # i = 0
                while stack and temperatures[TempInt] > temperatures[stack[-1]]:
                    output_number = stack.pop() # 0
                    # i++ # i = 1
                    # i approach is wrong 
                    # i think its the indexes
                    
                    output[output_number] = TempInt - output_number # 
                    # on the fifth iteration you will discover that
                    # you need to minus the indexes rather than 
                    # use the i approach or eltse you wont get 4 rather 3 
                    
                   
                # output[] # how to keep track of the index 
                stack.append(TempInt)


        return output
