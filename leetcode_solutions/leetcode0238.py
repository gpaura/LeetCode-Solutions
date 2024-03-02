class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]* (len(nums))
        
        prefix = 1
        for i in range(len(nums)):
            ans[i] = prefix
            prefix *= nums[i]
            
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= postfix
            postfix *= nums[i]
        
        return ans


# Time Complexity: O(n) where n is the length of the list nums.
# Space Complexity: O(1) , excluding the output array ans.