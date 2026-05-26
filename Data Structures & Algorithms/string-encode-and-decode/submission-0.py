class Solution:

    def delimeter(self, strs: str):
        return f"{len(strs)}#{strs}"

    def encode(self, strs: List[str]) -> str:
        # ["asim", "this", "that"] -> asim,this,that
        # 4455#then the word comes here        
        word = ""
        for i in strs:
            word += self.delimeter(i)
        return word

    def decode(self, s: str) -> List[str]:
        # abstr -> ["asim", "this", "that"]
        number = ""
        lst = []
        ipr = 0
        for i in range(len(s)):
            if ipr == 0:
                if s[i] != "#":
                    number += s[i]
                elif s[i] == "#":
                    localnum = int(number)
                    number = "0"
                    lst.append("")
                    ipr = localnum
            else:
                lst[-1]+= s[i]
                ipr-=1
        return lst

