

class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 1 # There is only one way to get to the first step
        current = 2 # There are only two ways to get to the second step

        if n < 3:
            return n

        for i in range(3, n + 1):
            next_value = current + prev

            prev = current
            current = next_value

        return current



if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(44))
