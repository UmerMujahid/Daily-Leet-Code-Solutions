class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1:
            return s

        col=0
        row=0
        j=0
        n=len(s)
        nums=[[0 for _ in range(n)] for _ in range(numRows)]
        while(True):
            if j==len(s):
                break
            for _ in range(numRows):
                if j==len(s):
                    break
                nums[row][col]=s[j]
                if row!=numRows-1:
                    row=row+1
                j=j+1
            if j==len(s):
                break
            while row!=1:
                col=col+1
                row=row-1
                if j==len(s):
                    break
                nums[row][col]=s[j]
                j=j+1

            col=col+1
            row=row-1

        result="" 
        for k in range(numRows):
            for z in range(n):
                if nums[k][z]!=0:
                    result+= nums[k][z]
            
        return result
