class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            s=0
            while nums[i] != 0:
                r = nums[i] % 10
                s += r
                nums[i] = nums[i] // 10
            if s==i:
                return i
            
        return -1

            
        