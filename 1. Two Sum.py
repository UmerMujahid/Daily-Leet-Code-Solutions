class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        total=len(nums)
        for i in range(total):
            for j in range (int(i+1),total):
                if nums[i]+nums[j]==target:
                    return [i,j]


nums = [2,7,11,15]
target=9
obj=Solution()
print(obj.twoSum(nums,target))
