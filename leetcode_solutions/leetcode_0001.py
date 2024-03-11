class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = []
        for i in range(len(nums)):
            for k in range(i + 1, len(nums)):
                if nums[i] + nums[k] == target:
                    a.append(i)
                    a.append(k)
                    break

        return a


# Time Complexity: O(n^2)
# Space Complexity: O(1)
# The time complexity is O(n^2) because the outer loop runs n times and the inner loop runs n - 1 times.
# The space complexity is O(1) because the space used is constant.