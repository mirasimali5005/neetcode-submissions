class Solution:
    def isPalindrome(self, s: str) -> bool:
        actual = ""
        for i in s:
            if i.isalnum():
                actual += i.lower()
        front = 0 
        back = len(actual) - 1
        # front and back pointer will keep going until they meet each other which is 
        # when back is less than front 
        while back > front:
            if actual[front] != actual[back]:
                return False
            back -= 1
            front += 1
        return True
    