class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        string=s.lstrip()
        if string=="":
            return 0
        
        number=""
        j=0
        flag=False
        sign=""

        if string[0]=="+" or string[0]=="-":
            sign=string[0]
            j=1
        
        number+=sign
        
        while j<len(string) and string[j]=='0':
            j+=1
        
        while j<len(string) and string[j].isdigit():
            number+=string[j]
            j+=1
        
        if number=="" or number=="+" or number=="-":
            return 0

        num=int(number)
        if (-2**31) <= num <= (2**31)-1:
            return num
        elif (-2**31) > num:
            num= -2**31
        else:
            num= (2**31)-1

        return num        
