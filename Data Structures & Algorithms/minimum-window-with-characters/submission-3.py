from collections import deque
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # first find the occurence
        # after the occurence we will move the window to the left and see if its valid 
        #  


        # s = "ADAOBECODEBANC"   len = 13

        # as long as the occurences of t is just enough we move left pointer
        
        verified = {}
        for i in t:
            if i in verified:
                verified[i] += 1
            else:
                verified[i] = 1

        req = len(verified)

        def check(hashmap):
            for key in verified:
                if key not in hashmap:
                    return False
                elif hashmap[key] < verified[key]:
                    return False
            return True
        notfound = "a" * (len(s) + 1)
        word = "a" * (len(s) + 1)
        l = 0 
        r = 0
        count = {}
        formed = 0
        while r < len(s) or formed == req:
            if formed < req:
                if s[r] in count:
                    count[s[r]] += 1
                else:
                    count[s[r]] = 1
                if s[r] in verified and count[s[r]] == verified[s[r]]:
                    formed += 1
                r += 1
            else:
                if len(s[l:r]) < len(word):
                    word = s[l:r]
                
                count[s[l]] -= 1
                if s[l] in verified and count[s[l]] < verified[s[l]]:
                    formed -= 1
                l += 1
        
        if check(count):
            if len(s[l:r]) < len(word):
                    word = s[l:r]

        if word == notfound:
            return ""
        else:
            return word
