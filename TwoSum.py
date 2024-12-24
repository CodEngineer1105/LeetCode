class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(0,len(nums)):
            d[nums[i]]=i
        for i in range(0,len(nums)):
            tmp=target-nums[i]
            if tmp in d.keys() and i!=d[tmp]:
                return [i,d[tmp]]
        return [-1,-1]
