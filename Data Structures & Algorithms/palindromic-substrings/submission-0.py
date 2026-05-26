class Solution:
    def countSubstrings(self, s: str) -> int:
        # we will use 2 pointer approach similar to the one 
        # we did in longest palindromic substring 

        output = len(s)

        
        for i in range(len(s)):
            # for the odd length
            l = i - 1
            r = i + 1 
            while l >= 0 and r < len(s) and s[l] == s[r]:
                output+=1
                l-=1
                r+=1
            
            # now for the even case
            l = i
            r = i+1
            while l >= 0 and r<len(s) and s[l] == s[r]:
                output+= 1
                l-=1
                r+=1
        return output
        # no need to use dp here since it doesnt make sense
        # to keep track of previous elements 
# like i undertsand the approach of storing true or false
# in a dp table but that is redundant 

        