class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        flag = False
        ind = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            tmp = float('inf')
            ind = i
            for j in range(i+1, len(nums)):
                if nums[i]<nums[j] and tmp>nums[j]:
                    jnd = j
                    tmp = nums[j]
                    flag = True
            if flag:
                nums[ind], nums[jnd] = nums[jnd], nums[ind]
                break
        if not flag:
            nums.sort()
            return
        tmp = nums[ind+1:]
        tmp.sort()
        for j in range(0,len(tmp)):
            nums[ind+1+j] = tmp[j]
        return
