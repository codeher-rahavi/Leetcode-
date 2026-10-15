class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        distinct =0 
        for i in range(len(nums)):
            for j in range(len(nums)+1):
                a=nums[i:j]
                count=len(list(set(a)))
                squared = count * count
                distinct +=squared
        
        return distinct

        