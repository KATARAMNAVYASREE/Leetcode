class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x

        low, high = 1, x
        ans = 0

        while low <= high:
            mid = (low + high) // 2
            square = mid * mid

            if square == x:
                return mid
            elif square < x:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans