class Solution:
   def characterReplacement(self, s: str, k: int) -> int:
       left, right = 0, 0
       frequency = [0] * 26 # uppercase English characters
      
       max_frequency = 0
      
       while right < len(s):
           frequency[ord(s[right]) - ord('A')] += 1
           max_frequency = max(max_frequency, frequency[ord(s[right]) - ord('A')])
          
           if (right - left + 1) > max_frequency + k:
               frequency[ord(s[left]) - ord('A')] -= 1
               left += 1
      
           right += 1
          
       return right - left

# Time complexity: O(n) where n is the length of the input string
# Space complexity: O(1) since the frequency array is of constant size