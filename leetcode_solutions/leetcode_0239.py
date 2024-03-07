from collections import deque # deque is a double-ended queue

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_nums = []
        index_queue = deque()

        for index, num in enumerate(nums):
            if index_queue and index - k + 1 > index_queue[0]:
                index_queue.popleft()

            while index_queue and nums[index_queue[-1]] <= num:
                index_queue.pop()

            index_queue.append(index)

            if index >= k - 1:
                max_nums.append(nums[index_queue[0]])

        return max_nums


# Time complexity: O(n) where n is the number of elements in the array nums.
# Space complexity: O(k) where k is the size of the sliding window.
