class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        """
        i=len(nums)-2
        j=len(nums)-1
        pivot=-1
        while (i>=0 and j>=0) and i<j:
            if nums[i]<nums[j]:
                pivot = i
                break
            i-=1
            j-=1
        arr = nums[pivot+1:]
        arr = sorted(arr)
        next_greater =-1
        for i in range(len(arr)):
            if arr[i]>nums[pivot]:
                next_greater=arr[i]
                break
        index =-1
        for i in range(pivot+1,len(nums)):
            if nums[i]==next_greater:
                index = i
                break
        temp = nums[pivot]
        nums[pivot] = nums[index]
        next_greater
        nums[index] = temp
        nums[pivot+1:]=sorted(nums[pivot+1:])
               
        