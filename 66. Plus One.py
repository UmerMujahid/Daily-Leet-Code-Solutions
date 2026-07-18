class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if len(digits)==0:
            return []
            
        temp=[str(d) for d in digits]
        print(temp)

        no="".join(temp)  
        print("no",no)

        no1=int(no)
        no1=no1+1
        print("no1",no1)

        str1=str(no1)
        print("str1",str1)
        result=[int(i) for i in str1]

        return result
