# Hard - 42. Trapping Rain Water

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0 # list is empty

        left, right = 0, len(height) - 1
        water = 0
        left_max, right_max = height[left], height[right]


        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water += right_max - height[right]

        return water

# Time Complexity: O(n) - n is the length of the input list
# Space Complexity: O(1) - no extra space is used
