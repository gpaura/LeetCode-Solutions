class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        contains_value = set()

        for num in nums:
            if num in contains_value:
                return True

            contains_value.add(num)
        
        return False

# Time Complexity: O(n) where n is the number of elements in the list.

# Space Complexity: O(n) because in the worst case, if all elements are unique, 
# the set would need to store all n elements separately from the original list.