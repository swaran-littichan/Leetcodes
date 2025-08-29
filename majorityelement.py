class Solution(object):
    def majorityElement(self, nums):
        count={}
        majority=len(nums)//2
        for i in nums:
             count[i]=count.get(i,0)+1
             if count[i]>majority:
                return i