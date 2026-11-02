class Solution:
    def reverse(self, n: int) -> int:
        if n < 0:
            sign = -1
            n = abs(n)
        else:
            sign = 1
        rev = 0
        while n > 0:
            digit = n % 10
            rev = rev * 10 + digit
            n //= 10
        rev = rev * sign
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        return  rev