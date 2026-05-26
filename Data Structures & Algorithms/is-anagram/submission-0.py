class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            keep = {}
            sec = {}
            for i in s:
                if i in keep:
                    keep[i] += 1
                else:
                    keep[i] = 1
            for i in t:
                if i in sec:
                    sec[i] += 1
                else:
                    sec[i] = 1
                
            for items in keep:
                if items not in sec or keep[items] != sec[items]:
                    return False
            return True
        else:
            return False