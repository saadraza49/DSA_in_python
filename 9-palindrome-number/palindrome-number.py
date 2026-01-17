class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = str(x)
        rev = ""
        for i in range(len(a)-1 , -1 , -1):
            rev += a[i]
        if a == rev:
            return True
        else:
            return False
