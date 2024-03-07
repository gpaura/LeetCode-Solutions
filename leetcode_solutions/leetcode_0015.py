''' Brute force
class Solution:
    def maxArea(self, height: List[int]) -> int:
        water = 0
        left, right = 0, 1

        if len(height) < 3:
            return height[0] * height[1]
        
        for left in range(len(height)-2):
            while right < len(height):
                amount_water = abs(right - left) * min(height[left], height[right])
                
                if amount_water > water:
                    water = amount_water
                right += 1
        
            right = left + 1
        
        return water
'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        water = 0
        left, right = 0, len(height) - 1
        
        while left < right:
            amount_water = abs(right - left) * min(height[left], height[right])
            water = max(amount_water, water)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return water

# Time Complexity: O(n) - n is the length of the input list
# Space Complexity: O(1) - no extra space is used