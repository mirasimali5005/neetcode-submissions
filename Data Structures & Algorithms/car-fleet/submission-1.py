class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 1 4 -> 4 6 -> 7 8 -> 10 10 so one fleet 


        # 4 1 0 7 -> 7 4 1 0 time = 3 3 4.5 10
        # 6 3 1 8
        # 8 5 2 9
        #10 7 3 10
        # hence 3 fleets
        # so time is 4 4 6 10
        
        stack = [] # this will give us the length at the end 
        # we create a hashmap linked to each of the speeds 
        # so that we can reference them
        posTOspeed = {}
        posTOtime = {}
        for i in range(len(position)):
            posTOspeed[position[i]] = speed[i]
            posTOtime[position[i]] = (target - position[i])/speed[i]

        position.sort(reverse=True)
        for pos in position:
            if not stack:
                stack.append(pos) 
            else:
                if posTOtime[pos] > posTOtime[stack[-1]]:
                    stack.append(pos)
        return len(stack)


    
