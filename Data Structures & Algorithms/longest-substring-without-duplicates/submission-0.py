class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # go left when you meet a duplicate 
        # keep the duplicate in a set so you can remove and
        # add and check for element which has already been seen
        # 
        sets = {} # a b c a
        l = 0
        r = 0
        output = 0
        while r < len(s):
            if s[r] in sets and l <= sets[s[r]] <= r:
                output = max(output, r - l)
                l = sets[s[r]] + 1
                sets[s[r]] = r
            else:
                sets[s[r]] = r

            r+=1
        output = max(output, r - l)
        # we have to check at final if set is empty properly
        return output