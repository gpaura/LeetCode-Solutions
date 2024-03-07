class Solution:
    def minWindow(self, s: str, t: str) -> str:

        min_left, left = -1, 0
        minimum_window = math.inf
        t_counter = Counter(t)
        window_counter = Counter()
        valid_char_count = 0

        for right, char in enumerate(s):

            window_counter[char] += 1

            if t_counter[char] >= window_counter[char]:
                valid_char_count += 1

            while valid_char_count == len(t):
                if right - left + 1 < minimum_window:
                    minimum_window = right - left + 1
                    min_left = left

                if t_counter[s[left]] >= window_counter[s[left]]:
                    valid_char_count -= 1

                window_counter[s[left]] -= 1
                left += 1

        return "" if min_left < 0 else s[min_left : min_left + minimum_window]

# Time complexity: O(n + m) where n is the length of the input string and m is the length of the input pattern
# Space complexity: O(n + m) where n is the length of the input string and m is the length of the input pattern
