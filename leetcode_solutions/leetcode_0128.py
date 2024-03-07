class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        values = set(nums)
        longest = 0
        
        for val in values:
            if val - 1 not in values:
                count = 1
                current_val = val + 1

                while current_val in values:
                    current_val += 1
                    count +=1

                longest = max(longest, count)
            
        return longest

# Time Complexity: O(n) to create the set and O(n) to iterate through the set on average 
# Space Complexity: O(n) because the values are stored in a set
