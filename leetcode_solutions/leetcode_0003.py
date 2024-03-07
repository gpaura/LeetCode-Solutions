class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sum = 0
        window_start = 0
        substring = []

        for window_end in range(len(s)):
            if s[window_end] not in substring:
                substring.append(s[window_end])
            else:
                sum = max(sum, len(substring))
                while s[window_start] != s[window_end]:
                    substring.pop(0)
                    window_start += 1
                substring.pop(0)
                window_start += 1
                substring.append(s[window_end])

        sum = max(sum, len(substring))
            
        return sum

# Time complexity: O(n)
# Space complexity: O(n)