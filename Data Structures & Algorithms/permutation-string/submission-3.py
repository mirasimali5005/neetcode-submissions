class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        perm = {}
        for letter in s1:
            if letter in perm:
                perm[letter] += 1
            else:
                perm[letter] = 1
        
        # s1 = "aabs"        s2 = "fsabsbaas"
        #                    s2 = "fsabqbaas"
        # s1 = "adc"         s2 = "dcda"
        l = 0
        r = 0
        length = len(s1)
        permtemp = {}
        forwardlen = length
        while r < len(s2):
            if s2[r] in perm:
                # window open
                if forwardlen > 0:
                    if s2[r] in permtemp:
                        permtemp[s2[r]] += 1
                    else:
                        permtemp[s2[r]] = 1
                    forwardlen -= 1
                    if permtemp == perm:
                        return True
                    r += 1
                else:
                    if permtemp == perm:
                        return True
                    permtemp[s2[l]] -= 1
                    if permtemp[s2[l]] == 0:
                        del permtemp[s2[l]]
                    l += 1
                    forwardlen += 1

                
            else:
                # when moving forward dont reset window just remove l and add the next element
                forwardlen = length
                permtemp = {}
                r += 1
                l = r
        return False
        
        
