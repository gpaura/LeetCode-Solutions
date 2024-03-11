class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(open_count, closed_count, ans):
            if open_count > n or closed_count > n or open_count < closed_count:
                return
            if open_count == n and closed_count == n:
                combinations.append(ans)

            backtrack(open_count + 1, closed_count, ans + "(")
            backtrack(open_count, closed_count + 1, ans + ")")

        combinations = []
        backtrack(0, 0, "")

        return combinations


# Time Complexity: O(4^n / sqrt(n)) 4^n / sqrt(n) is the n-th catalan number
# Space Complexity: O(n) Typically, the space complexity considers only the additional space required, not the space
# for the output. Therefore, we only consider the O(n) space used by the call stack for our space complexity analysis.