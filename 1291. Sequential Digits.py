class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        result=[]
        lst=[]
        valid="123456789"

        if low>high:
            return result

        for i in range(len(valid)):
          for j in range(i+1,len(valid)+1):
            lst.append(valid[i:j])
          
        for i in lst:
          no=int(i)
          if no >= low and no<=high:
            result.append(no)
        
        result.sort()
          
        return result
            
