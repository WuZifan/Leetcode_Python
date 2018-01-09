class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s=(x>0)-(x<0)
        x=s*x
        return x-int(str(x)[::-1])==0 and s!=-1