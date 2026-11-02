class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev=0
        num=x
        if x<0:
            return False
        else:
            while x>0:
                digit=x%10
                rev=rev*10+digit
                x=x//10
            if rev==num:
                return True
            else:
                return False


        