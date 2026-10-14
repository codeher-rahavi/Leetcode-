class Solution:
    def maxSumOfSquares(self, num: int, s: int) -> str:
        if s < 1 or s > num * 9:
            return ""

        ans = ""

        while num > 0:
            digit = min(s, 9)
            ans += str(digit)
            s -= digit
            num -= 1

        return ans