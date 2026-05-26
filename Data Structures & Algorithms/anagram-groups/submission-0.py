class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we could have a hashmap and loop through each item and loop again in the hasmap
        # to see if they match but this is very inefficient 
        # tea -> "t", "e", "a"
        # tea we would make 3c2 combinations
        # or we could sort them in alphabetical order 

        # if not strs[0]:
        #     return list([strs])
        words = {} # this will store the word and also store the index of where the ananogram is in the strs
        for i in range(len(strs)):
            sorted_word = "".join(sorted(strs[i], key=str.lower))
            if sorted_word not in words:
                words[sorted_word] = [strs[i]]
            else:
                words[sorted_word].append(strs[i])
            
        
        # we have to create the output string 
        output = []
        for i in words:
            output.append(words[i])
        return output