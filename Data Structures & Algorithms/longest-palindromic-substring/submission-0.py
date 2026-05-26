class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = {}
        for i in range(len(s)):
            l = i - 1 if i - 1 >= 0 else i
            r = i + 1 if i + 1 < len(s) else i
            # odd
            dp[i] = s[i]
            while l>= 0 and r< len(s) and s[l] == s[r]:
                dp[i] = s[l:r+1]
                l-=1
                r+=1
            # even
            # check right only since we go from left to right 
            l = i
            r = i + 1 if i + 1 < len(s) else i
            if r == i+1:
                temp = s[i]
                while l>= 0 and r < len(s) and s[r] == s[l]:
                    temp = s[l:r+1]
                    r += 1
                    l-=1
                if len(temp) > len(dp[i]):
                    dp[i] = temp
        answer = ""
        for i in dp:
            if len(dp[i]) > len(answer):
                answer = dp[i]
        return answer

            