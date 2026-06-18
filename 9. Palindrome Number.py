class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        stri=str(x)
        if len(stri)==1:
            return True
        if '-' in stri:
            return False

        y=stri[::-1]
        if x==int(y):
            return True
        else:
            return False

obj=Solution()
x=121
flag=obj.isPalindrome(x)
print(flag)
        
