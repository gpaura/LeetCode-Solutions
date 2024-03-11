class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []

        for index, current_temp in enumerate(temperatures):

            while stack and temperatures[stack[-1]] < current_temp:
                previous_index = stack.pop()
                answer[previous_index] = index - previous_index

            stack.append(index)

        return answer


# Time Complexity: The time complexity of the given code is O(N), where N is the number of days in the temperatures list.
# Space Complexity: The space complexity of the given code is O(N) as well, where N is the number of days in the temperatures list.