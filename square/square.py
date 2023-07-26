class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        if x == 1:
            return 1        
        guess = x // 2
        while guess * guess > x:
            guess = (guess + x // guess) // 2
        return guess
