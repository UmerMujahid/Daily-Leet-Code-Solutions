class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr=[]
        max_len=0

        if s=="":
            return 0
        if s==" ":
            return 1
        else:
            for i in s:
                if i in arr:
                    max_len = max(max_len, len(arr))
                    cut_off=arr.index(i)+1
                    arr=arr[cut_off:]

                arr.append(i)

            return max(max_len, len(arr))

        
