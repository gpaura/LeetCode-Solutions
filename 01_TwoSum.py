class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = []
        for i in range(len(nums)):
            for k in range(i+1,len(nums)):
                if (nums[i] + nums[k] == target):
                    a.append(i)
                    a.append(k)
                    break
        
        return a